"""
Prisma integration for Django REST API.
This module provides utilities to connect Django ORM models with Prisma Client.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from django.db import models
from django.utils import timezone
from typing import Any, Dict, List, Optional, Union

# Load environment variables from .env file
load_dotenv()

# Try to import Prisma client
try:
    from prisma import Prisma, PrismaClient
    prisma = PrismaClient()
except ImportError:
    print("Prisma client not installed. Please run: pip install prisma")
    prisma = None

class PrismaQuerySet:
    """
    A Django-like query interface for Prisma models.
    This class is meant to simulate common Django QuerySet methods.
    """
    
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = getattr(prisma, self.model_name.lower())
        self._filters = {}
        self._excludes = {}
        self._order_by = []
        self._limit = None
        self._offset = None
        self._select = {}
        self._include = {}
        
    def filter(self, **kwargs):
        """Filter records based on given parameters."""
        for key, value in kwargs.items():
            if '__' in key:
                field, operator = key.split('__', 1)
                if operator == 'contains':
                    self._filters[field] = {'contains': value}
                elif operator == 'gt':
                    self._filters[field] = {'gt': value}
                elif operator == 'gte':
                    self._filters[field] = {'gte': value}
                elif operator == 'lt':
                    self._filters[field] = {'lt': value}
                elif operator == 'lte':
                    self._filters[field] = {'lte': value}
                elif operator == 'in':
                    self._filters[field] = {'in': value}
                else:
                    self._filters[key] = value
            else:
                self._filters[key] = value
        return self
    
    def exclude(self, **kwargs):
        """Exclude records based on given parameters."""
        for key, value in kwargs.items():
            if key in self._filters:
                continue  # Skip if already defined in filters
            self._excludes[key] = value
        return self
    
    def order_by(self, *fields):
        """Order records by given fields."""
        for field in fields:
            if field.startswith('-'):
                self._order_by.append({field[1:]: 'desc'})
            else:
                self._order_by.append({field: 'asc'})
        return self
    
    def limit(self, value):
        """Limit the number of returned records."""
        self._limit = value
        return self
    
    def offset(self, value):
        """Skip the first N records."""
        self._offset = value
        return self
    
    def select(self, *fields):
        """Select only specific fields."""
        for field in fields:
            self._select[field] = True
        return self
    
    def include(self, **relations):
        """Include related models."""
        for rel, value in relations.items():
            if isinstance(value, bool) and value:
                self._include[rel] = True
            elif isinstance(value, dict):
                self._include[rel] = value
        return self
    
    def _build_where(self):
        """Build the where clause from filters and excludes."""
        where = {}
        
        # Add filters
        if self._filters:
            for key, value in self._filters.items():
                where[key] = value
        
        # Add excludes as NOT conditions
        if self._excludes:
            for key, value in self._excludes.items():
                where[f"NOT_{key}"] = value
                
        # Always exclude soft-deleted records
        where['deletedAt'] = None
        
        return where if where else None
    
    def _build_query_args(self):
        """Build the query arguments for Prisma."""
        args = {}
        
        # Where conditions
        where = self._build_where()
        if where:
            args['where'] = where
        
        # Order by
        if self._order_by:
            args['order_by'] = self._order_by
        
        # Pagination
        if self._limit is not None:
            args['take'] = self._limit
        if self._offset is not None:
            args['skip'] = self._offset
        
        # Select fields
        if self._select:
            args['select'] = self._select
        
        # Include relations
        if self._include:
            args['include'] = self._include
        
        return args
    
    async def all(self):
        """Get all records that match the current filters."""
        if not prisma:
            return []
        
        args = self._build_query_args()
        return await self.model.find_many(**args)
    
    async def get(self, **kwargs):
        """Get a single record that matches the filters."""
        if not prisma:
            return None
        
        # Add any additional filters
        for key, value in kwargs.items():
            self._filters[key] = value
        
        args = self._build_query_args()
        return await self.model.find_first(**args)
    
    async def create(self, **kwargs):
        """Create a new record."""
        if not prisma:
            return None
        
        # Remove any fields that should not be set directly
        kwargs.pop('id', None)  # ID is auto-generated
        kwargs.pop('createdAt', None)  # These are handled by Prisma
        kwargs.pop('updatedAt', None)
        kwargs.pop('deletedAt', None)
        
        return await self.model.create(data=kwargs)
    
    async def update(self, **kwargs):
        """Update records that match the current filters."""
        if not prisma:
            return 0
        
        # Remove any fields that should not be updated directly
        kwargs.pop('id', None)
        kwargs.pop('createdAt', None)
        kwargs.pop('deletedAt', None)
        
        # Always set updatedAt to now
        kwargs['updatedAt'] = timezone.now()
        
        where = self._build_where()
        if not where:
            return 0  # No filters, don't allow update of all records
        
        result = await self.model.update_many(
            where=where,
            data=kwargs
        )
        return result.count if hasattr(result, 'count') else 0
    
    async def delete(self, hard_delete=False):
        """
        Delete records that match the current filters.
        By default, this is a soft delete (sets deletedAt).
        If hard_delete is True, performs an actual delete.
        """
        if not prisma:
            return 0
        
        where = self._build_where()
        if not where:
            return 0  # No filters, don't allow deletion of all records
        
        if hard_delete:
            # Perform hard delete
            result = await self.model.delete_many(where=where)
        else:
            # Perform soft delete
            result = await self.model.update_many(
                where=where,
                data={'deletedAt': timezone.now()}
            )
        
        return result.count if hasattr(result, 'count') else 0
    
    async def count(self):
        """Count records that match the current filters."""
        if not prisma:
            return 0
        
        where = self._build_where()
        count = await self.model.count(where=where) if where else await self.model.count()
        return count


class PrismaModel:
    """
    Base class for Prisma models in Django.
    This class provides an interface similar to Django models but using Prisma underneath.
    """
    
    # The name of the Prisma model
    model_name = None
    
    @classmethod
    def objects(cls):
        """Return a QuerySet-like object for this model."""
        if not cls.model_name:
            cls.model_name = cls.__name__
        return PrismaQuerySet(cls.model_name)
    
    @classmethod
    async def create(cls, **kwargs):
        """Create a new record."""
        return await cls.objects().create(**kwargs)
    
    @classmethod
    async def get(cls, **kwargs):
        """Get a single record by filters."""
        return await cls.objects().get(**kwargs)
    
    @classmethod
    async def filter(cls, **kwargs):
        """Filter records."""
        return await cls.objects().filter(**kwargs).all()
    
    @classmethod
    async def all(cls):
        """Get all records."""
        return await cls.objects().all()
    
    @classmethod
    async def count(cls):
        """Count all records."""
        return await cls.objects().count()


# Example usage with Django models:
# class User(models.Model, PrismaModel):
#     model_name = "User"
#     # Django model fields...
#     
#     class Meta:
#         db_table = "users"
#         verbose_name = "User"
#         verbose_name_plural = "Users"
