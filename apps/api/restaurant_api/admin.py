"""
Admin configuration for the Restaurant API.
"""

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    User, Restaurant, RestaurantImage, Menu, MenuCategory, 
    MenuItem, Table, Review
)


class SoftDeleteAdmin(admin.ModelAdmin):
    """Base admin class for models with soft delete."""
    
    list_display = ('__str__', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    
    def get_queryset(self, request):
        """Include soft-deleted objects in admin."""
        qs = self.model.objects.all()  # Get all objects including deleted ones
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


@admin.register(User)
class UserAdmin(SoftDeleteAdmin):
    """Admin for the User model."""
    
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'created_at', 'deleted_at')
    list_filter = ('role', 'is_active', 'created_at', 'deleted_at')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('created_at', 'updated_at', 'deleted_at')}),
    )
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')


class RestaurantImageInline(admin.TabularInline):
    """Inline for restaurant images."""
    model = RestaurantImage
    extra = 1
    fields = ('image_url', 'alt_text', 'is_primary')
    readonly_fields = ('created_at', 'updated_at')


class MenuInline(admin.TabularInline):
    """Inline for restaurant menus."""
    model = Menu
    extra = 1
    fields = ('name', 'description', 'is_active')
    readonly_fields = ('created_at', 'updated_at')


class TableInline(admin.TabularInline):
    """Inline for restaurant tables."""
    model = Table
    extra = 1
    fields = ('table_number', 'capacity', 'location', 'is_available')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Restaurant)
class RestaurantAdmin(SoftDeleteAdmin):
    """Admin for the Restaurant model."""
    
    list_display = ('name', 'city', 'country', 'owner_email', 'rating', 'is_active', 'is_verified', 'created_at', 'deleted_at')
    list_filter = ('is_active', 'is_verified', 'price_range', 'created_at', 'deleted_at')
    search_fields = ('name', 'description', 'address', 'city', 'country')
    ordering = ('-created_at',)
    inlines = [RestaurantImageInline, MenuInline, TableInline]
    
    def owner_email(self, obj):
        """Get the email of the restaurant owner."""
        return obj.owner.email if obj.owner else '-'
    owner_email.short_description = 'Owner'


class MenuCategoryInline(admin.TabularInline):
    """Inline for menu categories."""
    model = MenuCategory
    extra = 1
    fields = ('name', 'description', 'display_order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Menu)
class MenuAdmin(SoftDeleteAdmin):
    """Admin for the Menu model."""
    
    list_display = ('name', 'restaurant_name', 'is_active', 'created_at', 'deleted_at')
    list_filter = ('is_active', 'created_at', 'deleted_at')
    search_fields = ('name', 'description', 'restaurant__name')
    ordering = ('-created_at',)
    inlines = [MenuCategoryInline]
    
    def restaurant_name(self, obj):
        """Get the name of the restaurant."""
        return obj.restaurant.name if obj.restaurant else '-'
    restaurant_name.short_description = 'Restaurant'


class MenuItemInline(admin.TabularInline):
    """Inline for menu items."""
    model = MenuItem
    extra = 1
    fields = ('name', 'price', 'is_vegetarian', 'is_vegan', 'is_gluten_free', 'is_available', 'display_order')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MenuCategory)
class MenuCategoryAdmin(SoftDeleteAdmin):
    """Admin for the MenuCategory model."""
    
    list_display = ('name', 'menu_name', 'restaurant_name', 'display_order', 'is_active', 'created_at', 'deleted_at')
    list_filter = ('is_active', 'created_at', 'deleted_at')
    search_fields = ('name', 'description', 'menu__name', 'menu__restaurant__name')
    ordering = ('menu__restaurant', 'menu', 'display_order')
    inlines = [MenuItemInline]
    
    def menu_name(self, obj):
        """Get the name of the menu."""
        return obj.menu.name if obj.menu else '-'
    menu_name.short_description = 'Menu'
    
    def restaurant_name(self, obj):
        """Get the name of the restaurant."""
        return obj.menu.restaurant.name if obj.menu and obj.menu.restaurant else '-'
    restaurant_name.short_description = 'Restaurant'


@admin.register(MenuItem)
class MenuItemAdmin(SoftDeleteAdmin):
    """Admin for the MenuItem model."""
    
    list_display = ('name', 'category_name', 'restaurant_name', 'price', 'dietary_info', 'is_available', 'created_at', 'deleted_at')
    list_filter = ('is_vegetarian', 'is_vegan', 'is_gluten_free', 'is_available', 'created_at', 'deleted_at')
    search_fields = ('name', 'description', 'ingredients', 'category__name', 'category__menu__name', 'category__menu__restaurant__name')
    ordering = ('category__menu__restaurant', 'category__menu', 'category', 'display_order')
    
    def category_name(self, obj):
        """Get the name of the category."""
        return obj.category.name if obj.category else '-'
    category_name.short_description = 'Category'
    
    def restaurant_name(self, obj):
        """Get the name of the restaurant."""
        return obj.category.menu.restaurant.name if obj.category and obj.category.menu and obj.category.menu.restaurant else '-'
    restaurant_name.short_description = 'Restaurant'
    
    def dietary_info(self, obj):
        """Display dietary information icons."""
        icons = []
        if obj.is_vegetarian:
            icons.append('🥗')  # Vegetarian
        if obj.is_vegan:
            icons.append('🌱')  # Vegan
        if obj.is_gluten_free:
            icons.append('🌾')  # Gluten-Free
        return ' '.join(icons) if icons else '-'
    dietary_info.short_description = 'Dietary'


@admin.register(Table)
class TableAdmin(SoftDeleteAdmin):
    """Admin for the Table model."""
    
    list_display = ('table_number', 'restaurant_name', 'capacity', 'location', 'is_available', 'created_at', 'deleted_at')
    list_filter = ('location', 'is_available', 'created_at', 'deleted_at')
    search_fields = ('table_number', 'restaurant__name')
    ordering = ('restaurant', 'table_number')
    
    def restaurant_name(self, obj):
        """Get the name of the restaurant."""
        return obj.restaurant.name if obj.restaurant else '-'
    restaurant_name.short_description = 'Restaurant'


@admin.register(Review)
class ReviewAdmin(SoftDeleteAdmin):
    """Admin for the Review model."""
    
    list_display = ('id', 'user_email', 'restaurant_name', 'rating_stars', 'created_at', 'deleted_at')
    list_filter = ('rating', 'created_at', 'deleted_at')
    search_fields = ('user__email', 'restaurant__name', 'comment')
    ordering = ('-created_at',)
    
    def user_email(self, obj):
        """Get the email of the user."""
        return obj.user.email if obj.user else '-'
    user_email.short_description = 'User'
    
    def restaurant_name(self, obj):
        """Get the name of the restaurant."""
        return obj.restaurant.name if obj.restaurant else '-'
    restaurant_name.short_description = 'Restaurant'
    
    def rating_stars(self, obj):
        """Display rating as stars."""
        return '⭐' * obj.rating if obj.rating else '-'
    rating_stars.short_description = 'Rating'
