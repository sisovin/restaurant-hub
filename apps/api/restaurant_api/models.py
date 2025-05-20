"""
Models for the Restaurant API.
"""

import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserRole(models.TextChoices):
    """User role choices."""
    USER = 'USER', 'User'
    OWNER = 'OWNER', 'Restaurant Owner'
    STAFF = 'STAFF', 'Restaurant Staff'
    ADMIN = 'ADMIN', 'Admin'


class PriceRange(models.TextChoices):
    """Price range choices for restaurants."""
    INEXPENSIVE = '$', 'Inexpensive'
    MODERATE = '$$', 'Moderate'
    EXPENSIVE = '$$$', 'Expensive'
    VERY_EXPENSIVE = '$$$$', 'Very Expensive'


class TableLocation(models.TextChoices):
    """Table location choices."""
    INDOOR = 'INDOOR', 'Indoor'
    OUTDOOR = 'OUTDOOR', 'Outdoor'
    PATIO = 'PATIO', 'Patio'
    BAR = 'BAR', 'Bar'
    PRIVATE = 'PRIVATE', 'Private Room'


class UserManager(BaseUserManager):
    """Custom user manager for the User model."""
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular user with the given email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', UserRole.ADMIN)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model that uses email for authentication."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        """Return the user's first name."""
        return self.first_name


class Restaurant(models.Model):
    """Restaurant model that represents a restaurant entity."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=255)
    price_range = models.CharField(
        max_length=20,
        choices=PriceRange.choices,
        default=PriceRange.MODERATE
    )
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    rating = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')

    class Meta:
        db_table = 'restaurants'
    
    def __str__(self):
        return self.name


class RestaurantImage(models.Model):
    """Restaurant image model to store images related to a restaurant."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_url = models.URLField()
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'restaurant_images'
    
    def __str__(self):
        return f"Image for {self.restaurant.name}"


class Menu(models.Model):
    """Menu model that represents a restaurant's menu."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')

    class Meta:
        db_table = 'menus'
    
    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"


class MenuCategory(models.Model):
    """Menu category model that groups menu items."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        db_table = 'menu_categories'
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.menu.name}"


class MenuItem(models.Model):
    """Menu item model that represents a dish on a menu."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    allergens = models.TextField(blank=True, null=True)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    spicy_level = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    class Meta:
        db_table = 'menu_items'
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"


class Table(models.Model):
    """Table model that represents a physical table in a restaurant."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    location = models.CharField(
        max_length=20,
        choices=TableLocation.choices,
        default=TableLocation.INDOOR
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')

    class Meta:
        db_table = 'tables'
        unique_together = ['restaurant', 'table_number']
    
    def __str__(self):
        return f"Table {self.table_number} at {self.restaurant.name}"


class Review(models.Model):
    """Review model for restaurant reviews."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        db_table = 'reviews'
        ordering = ['-created_at']
        unique_together = ['user', 'restaurant']
    
    def __str__(self):
        return f"Review for {self.restaurant.name} - {self.rating} stars"
