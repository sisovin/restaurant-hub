"""
Serializers for the Restaurant API.
"""

from rest_framework import serializers
from .models import (
    User, Restaurant, RestaurantImage, Menu, MenuCategory, 
    MenuItem, Table, Review
)


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone_number', 
            'role', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        """Create and return a new user with encrypted password."""
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user
    
    def update(self, instance, validated_data):
        """Update a user, setting the password correctly."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user


class RestaurantImageSerializer(serializers.ModelSerializer):
    """Serializer for the RestaurantImage model."""
    
    class Meta:
        model = RestaurantImage
        fields = [
            'id', 'image_url', 'alt_text', 'is_primary', 
            'restaurant', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TableSerializer(serializers.ModelSerializer):
    """Serializer for the Table model."""
    
    class Meta:
        model = Table
        fields = [
            'id', 'table_number', 'capacity', 'is_available', 
            'location', 'restaurant', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer for the MenuItem model."""
    
    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'description', 'price', 'image_url', 'ingredients',
            'allergens', 'is_vegetarian', 'is_vegan', 'is_gluten_free',
            'spicy_level', 'is_available', 'display_order', 'category',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MenuCategorySerializer(serializers.ModelSerializer):
    """Serializer for the MenuCategory model."""
    
    items = MenuItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = MenuCategory
        fields = [
            'id', 'name', 'description', 'display_order', 
            'is_active', 'menu', 'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MenuSerializer(serializers.ModelSerializer):
    """Serializer for the Menu model."""
    
    categories = MenuCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Menu
        fields = [
            'id', 'name', 'description', 'is_active',
            'restaurant', 'categories', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for the Restaurant model."""
    
    images = RestaurantImageSerializer(many=True, read_only=True)
    menus = MenuSerializer(many=True, read_only=True)
    tables = TableSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'description', 'address', 'city', 'state',
            'country', 'postal_code', 'phone_number', 'email', 'website',
            'cuisine_type', 'price_range', 'is_active',
            'is_verified', 'rating', 'owner', 'images', 'menus', 'tables',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'rating']





class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the Review model."""
    
    class Meta:
        model = Review
        fields = [
            'id', 'rating', 'comment', 
            'user', 'restaurant', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
