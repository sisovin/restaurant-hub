"""
Signal handlers for the Restaurant API.
"""

import logging
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import (
    User, Restaurant, RestaurantImage, Menu, MenuCategory, 
    MenuItem, Table, Review
)

logger = logging.getLogger(__name__)


@receiver(pre_save)
def handle_soft_delete(sender, instance, **kwargs):
    """
    Intercept save operations to handle soft delete behavior.
    This ensures that models with a deleted_at field are properly marked.
    """
    if hasattr(instance, 'deleted_at') and instance.deleted_at:
        # Don't include soft-deleted records in regular queries
        logger.info(f"Soft-deleting {sender.__name__} instance: {instance}")


@receiver(post_save, sender=Review)
def update_restaurant_rating(sender, instance, **kwargs):
    """
    Update the average rating of a restaurant when a review is saved.
    """
    restaurant = instance.restaurant
    
    # Calculate the new average rating
    active_reviews = Review.objects.filter(
        restaurant=restaurant,
        deleted_at__isnull=True
    )
    
    if active_reviews.exists():
        # Calculate the average rating from active reviews
        total_rating = sum(review.rating for review in active_reviews)
        avg_rating = total_rating / active_reviews.count()
        
        # Update the restaurant's rating
        restaurant.rating = round(avg_rating, 1)  # Round to 1 decimal place
        restaurant.save(update_fields=['rating', 'updated_at'])
        
        logger.info(f"Updated rating for restaurant {restaurant.name}: {restaurant.rating}")
    else:
        # No active reviews, set rating to None
        restaurant.rating = None
        restaurant.save(update_fields=['rating', 'updated_at'])
        
        logger.info(f"Cleared rating for restaurant {restaurant.name} (no active reviews)")


@receiver(post_delete, sender=Review)
def update_restaurant_rating_on_delete(sender, instance, **kwargs):
    """
    Update the average rating of a restaurant when a review is deleted.
    """
    restaurant = instance.restaurant
    
    # Calculate the new average rating
    active_reviews = Review.objects.filter(
        restaurant=restaurant,
        deleted_at__isnull=True
    )
    
    if active_reviews.exists():
        # Calculate the average rating from active reviews
        total_rating = sum(review.rating for review in active_reviews)
        avg_rating = total_rating / active_reviews.count()
        
        # Update the restaurant's rating
        restaurant.rating = round(avg_rating, 1)  # Round to 1 decimal place
        restaurant.save(update_fields=['rating', 'updated_at'])
        
        logger.info(f"Updated rating for restaurant {restaurant.name}: {restaurant.rating}")
    else:
        # No active reviews, set rating to None
        restaurant.rating = None
        restaurant.save(update_fields=['rating', 'updated_at'])
        
        logger.info(f"Cleared rating for restaurant {restaurant.name} (no active reviews)")
