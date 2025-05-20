"""
URL patterns for the Restaurant API.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')
router.register(r'restaurant-images', views.RestaurantImageViewSet, basename='restaurant-image')
router.register(r'menus', views.MenuViewSet, basename='menu')
router.register(r'menu-categories', views.MenuCategoryViewSet, basename='menu-category')
router.register(r'menu-items', views.MenuItemViewSet, basename='menu-item')
router.register(r'tables', views.TableViewSet, basename='table')
router.register(r'reviews', views.ReviewViewSet, basename='review')

# The API URLs are determined automatically by the router
urlpatterns = [
    # API Overview page as the root route
    path('', views.api_overview, name='api-overview'),
    # Include the router generated URLs
    path('', include(router.urls)),
]
