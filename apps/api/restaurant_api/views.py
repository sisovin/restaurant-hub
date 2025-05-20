"""Views for the Restaurant API."""

from rest_framework import viewsets, filters, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.reverse import reverse
from django.utils import timezone
from django.db.models import Q, Avg, Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    User, Restaurant, RestaurantImage, Menu, MenuCategory, 
    MenuItem, Table, Review, UserRole
)
from .serializers import (
    UserSerializer, RestaurantSerializer, RestaurantImageSerializer,
    MenuSerializer, MenuCategorySerializer, MenuItemSerializer,    
    TableSerializer, ReviewSerializer
)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_overview(request, format=None):
    """
    API overview endpoint providing links to all available endpoints.
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'restaurants': reverse('restaurant-list', request=request, format=format),
        'restaurant_images': reverse('restaurant-image-list', request=request, format=format),
        'menus': reverse('menu-list', request=request, format=format),
        'menu_categories': reverse('menu-category-list', request=request, format=format),
        'menu_items': reverse('menu-item-list', request=request, format=format),
        'tables': reverse('table-list', request=request, format=format),
        'reviews': reverse('review-list', request=request, format=format),
    })


class StandardResultsSetPagination(PageNumberPagination):
    """Standard pagination for API results."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ReadOnlyPublicPermissionMixin:
    """
    Mixin to allow anonymous access for list and retrieve actions,
    but require authentication for all other actions.
    """
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()


class SoftDeleteViewSetMixin:
    """Mixin to handle soft delete functionality."""
    
    def perform_destroy(self, instance):
        """Perform a soft delete by setting the deleted_at field."""
        instance.deleted_at = timezone.now()
        instance.save()
    
    @action(detail=False, methods=['get'])
    def deleted(self, request):
        """List all soft-deleted objects."""
        if not self.request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to view deleted items."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        queryset = self.get_queryset().filter(deleted_at__isnull=False)
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        """Restore a soft-deleted object."""
        if not self.request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to restore items."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        instance = self.get_object()
        instance.deleted_at = None
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserViewSet(SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the User model."""
    
    queryset = User.objects.filter(deleted_at__isnull=True)
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['email', 'first_name', 'last_name']
    ordering_fields = ['email', 'first_name', 'last_name', 'created_at']
    ordering = ['email']
    filterset_fields = ['role', 'is_active']

    def get_queryset(self):
        """Filter queryset based on user role."""
        queryset = super().get_queryset()
        
        # Regular users can only see themselves
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            queryset = queryset.filter(id=self.request.user.id)
        
        return queryset
        
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get the current user's profile."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
        
    @action(detail=False, methods=['get'])
    def owners(self, request):
        """List all restaurant owners."""
        if not request.user.is_staff and not request.user.is_superuser:
            return Response(
                {"detail": "You do not have permission to view this list."},
                status=status.HTTP_403_FORBIDDEN
            )
            
        owners = User.objects.filter(role=UserRole.OWNER, deleted_at__isnull=True)
        page = self.paginate_queryset(owners)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = self.get_serializer(owners, many=True)
        return Response(serializer.data)
        
    @action(detail=True, methods=['get'])
    def restaurants(self, request, pk=None):
        """Get all restaurants owned by a user."""
        user = self.get_object()
        
        # Only staff or the user themselves can see their restaurants
        if not request.user.is_staff and not request.user.is_superuser and request.user.id != user.id:
            return Response(
                {"detail": "You do not have permission to view this user's restaurants."},
                status=status.HTTP_403_FORBIDDEN
            )
            
        restaurants = Restaurant.objects.filter(owner=user, deleted_at__isnull=True)
        serializer = RestaurantSerializer(restaurants, many=True, context={'request': request})
        return Response(serializer.data)
        
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Get all reviews by a user."""
        user = self.get_object()
        
        # Only staff or the user themselves can see their reviews
        if not request.user.is_staff and not request.user.is_superuser and request.user.id != user.id:
            return Response(
                {"detail": "You do not have permission to view this user's reviews."},
                status=status.HTTP_403_FORBIDDEN
            )
            
        reviews = Review.objects.filter(user=user, deleted_at__isnull=True)
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)


class RestaurantViewSet(ReadOnlyPublicPermissionMixin, SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the Restaurant model."""
    
    queryset = Restaurant.objects.filter(deleted_at__isnull=True, is_active=True)
    serializer_class = RestaurantSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'cuisine_type', 'city', 'country']
    ordering_fields = ['name', 'rating', 'price_range', 'created_at']
    ordering = ['name']
    filterset_fields = ['price_range', 'cuisine_type', 'city', 'country', 'is_verified']

    def get_queryset(self):
        """Filter queryset based on query parameters."""
        queryset = super().get_queryset()
        
        # Get query parameters
        cuisine = self.request.query_params.get('cuisine', None)
        price_range = self.request.query_params.get('price_range', None)
        city = self.request.query_params.get('city', None)
        rating = self.request.query_params.get('rating', None)
        country = self.request.query_params.get('country', None)
        min_rating = self.request.query_params.get('min_rating', None)
        max_rating = self.request.query_params.get('max_rating', None)
        owner_id = self.request.query_params.get('owner_id', None)
        has_vegetarian = self.request.query_params.get('has_vegetarian', None)
        
        # Apply filters if parameters are provided
        if cuisine:
            queryset = queryset.filter(cuisine_type__icontains=cuisine)
        
        if price_range:
            queryset = queryset.filter(price_range=price_range)
        
        if city:
            queryset = queryset.filter(city__icontains=city)
        
        if country:
            queryset = queryset.filter(country__icontains=country)
        
        if rating:
            try:
                rating = float(rating)
                queryset = queryset.filter(rating__gte=rating)
            except ValueError:
                pass
                
        if min_rating:
            try:
                min_rating = float(min_rating)
                queryset = queryset.filter(rating__gte=min_rating)
            except ValueError:
                pass
                
        if max_rating:
            try:
                max_rating = float(max_rating)
                queryset = queryset.filter(rating__lte=max_rating)
            except ValueError:
                pass
                
        if owner_id:
            queryset = queryset.filter(owner__id=owner_id)
            
        if has_vegetarian and has_vegetarian.lower() == 'true':            # Find restaurants with vegetarian menu items
            queryset = queryset.filter(
                menus__categories__items__is_vegetarian=True
            ).distinct()
        
        return queryset
        
    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        """Get statistics for a restaurant.
        
        Returns the number of reviews, average rating, menu items count,
        and other useful statistics for restaurant owners.
        """
        restaurant = self.get_object()
        
        # Check if user has permission (only owner or staff)
        if not request.user.is_staff and not request.user.is_superuser and restaurant.owner != request.user:
            return Response(
                {"detail": "You do not have permission to view these statistics."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Calculate statistics
        # Get review stats
        review_stats = Review.objects.filter(restaurant=restaurant, deleted_at__isnull=True).aggregate(
            review_count=Count('id'),
            avg_rating=Avg('rating')
        )
        
        # Get menu and item counts
        menu_count = Menu.objects.filter(restaurant=restaurant, deleted_at__isnull=True).count()
        menu_item_count = MenuItem.objects.filter(
            category__menu__restaurant=restaurant, 
            deleted_at__isnull=True
        ).count()
        
        # Get dietary restriction counts
        dietary_counts = MenuItem.objects.filter(
            category__menu__restaurant=restaurant, 
            deleted_at__isnull=True
        ).aggregate(
            vegetarian_count=Count('id', filter=Q(is_vegetarian=True)),
            vegan_count=Count('id', filter=Q(is_vegan=True)),
            gluten_free_count=Count('id', filter=Q(is_gluten_free=True))
        )
        
        # Get table stats
        table_stats = Table.objects.filter(restaurant=restaurant, deleted_at__isnull=True).aggregate(
            table_count=Count('id'),
            available_count=Count('id', filter=Q(is_available=True)),
            total_capacity=Sum('capacity')
        )
        
        # Compile and return all stats
        stats = {
            'restaurant_id': restaurant.id,
            'restaurant_name': restaurant.name,
            'review_count': review_stats['review_count'] or 0,
            'average_rating': review_stats['avg_rating'] or 0,
            'menu_count': menu_count,
            'menu_item_count': menu_item_count,
            'vegetarian_items': dietary_counts['vegetarian_count'] or 0,
            'vegan_items': dietary_counts['vegan_count'] or 0,
            'gluten_free_items': dietary_counts['gluten_free_count'] or 0,
            'table_count': table_stats['table_count'] or 0,
            'available_tables': table_stats['available_count'] or 0,
            'total_seating_capacity': table_stats['total_capacity'] or 0
        }
        
        return Response(stats)


class RestaurantImageViewSet(SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the RestaurantImage model."""
    
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['is_primary', 'created_at']
    ordering = ['-is_primary', 'created_at']


class MenuViewSet(ReadOnlyPublicPermissionMixin, SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the Menu model."""
    
    queryset = Menu.objects.filter(is_active=True)
    serializer_class = MenuSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class MenuCategoryViewSet(SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the MenuCategory model."""
    
    queryset = MenuCategory.objects.filter(is_active=True)
    serializer_class = MenuCategorySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['display_order', 'name', 'created_at']
    ordering = ['display_order', 'name']


class MenuItemViewSet(ReadOnlyPublicPermissionMixin, SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the MenuItem model."""
    
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'ingredients']
    ordering_fields = ['display_order', 'name', 'price', 'created_at']
    ordering = ['display_order', 'name']
    filterset_fields = ['is_vegetarian', 'is_vegan', 'is_gluten_free', 'spicy_level', 'category']

    def get_queryset(self):
        """Filter queryset based on query parameters."""
        queryset = super().get_queryset()
        
        # Get query parameters
        category = self.request.query_params.get('category', None)
        vegetarian = self.request.query_params.get('vegetarian', None)
        vegan = self.request.query_params.get('vegan', None)
        gluten_free = self.request.query_params.get('gluten_free', None)
        spicy_level = self.request.query_params.get('spicy_level', None)
        max_price = self.request.query_params.get('max_price', None)
        min_price = self.request.query_params.get('min_price', None)
        restaurant_id = self.request.query_params.get('restaurant_id', None)
        
        # Apply filters if parameters are provided
        if category:
            queryset = queryset.filter(category__id=category)
        
        if vegetarian == 'true':
            queryset = queryset.filter(is_vegetarian=True)
        
        if vegan == 'true':
            queryset = queryset.filter(is_vegan=True)
        
        if gluten_free == 'true':
            queryset = queryset.filter(is_gluten_free=True)
        
        if spicy_level:
            try:
                level = int(spicy_level)
                queryset = queryset.filter(spicy_level__lte=level)
            except ValueError:
                pass
                
        if max_price:
            try:
                price = float(max_price)
                queryset = queryset.filter(price__lte=price)
            except ValueError:
                pass
                
        if min_price:
            try:
                price = float(min_price)
                queryset = queryset.filter(price__gte=price)
            except ValueError:
                pass
                
        if restaurant_id:
            queryset = queryset.filter(category__menu__restaurant__id=restaurant_id)
        
        return queryset


class TableViewSet(SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the Table model."""
    
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['table_number', 'capacity', 'is_available']
    ordering = ['table_number']
    filterset_fields = ['is_available', 'location', 'restaurant']

    def get_queryset(self):
        """Filter queryset based on query parameters."""
        queryset = super().get_queryset()
        
        # Get query parameters
        restaurant = self.request.query_params.get('restaurant', None)
        capacity = self.request.query_params.get('capacity', None)
        min_capacity = self.request.query_params.get('min_capacity', None)
        available = self.request.query_params.get('available', None)
        location = self.request.query_params.get('location', None)
        
        # Apply filters if parameters are provided
        if restaurant:
            queryset = queryset.filter(restaurant__id=restaurant)
        
        if capacity:
            try:
                cap = int(capacity)
                queryset = queryset.filter(capacity__gte=cap)
            except ValueError:
                pass
                
        if min_capacity:
            try:
                min_cap = int(min_capacity)
                queryset = queryset.filter(capacity__gte=min_cap)
            except ValueError:
                pass
        
        if available == 'true':
            queryset = queryset.filter(is_available=True)
        
        if location:
            queryset = queryset.filter(location=location)
        
        return queryset


class ReviewViewSet(ReadOnlyPublicPermissionMixin, SoftDeleteViewSetMixin, viewsets.ModelViewSet):
    """ViewSet for the Review model."""
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['comment']
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']
    filterset_fields = ['rating', 'restaurant', 'user']

    def get_queryset(self):
        """Filter queryset based on query parameters."""
        queryset = super().get_queryset()
        
        # Get query parameters
        restaurant = self.request.query_params.get('restaurant', None)
        user = self.request.query_params.get('user', None)
        rating = self.request.query_params.get('rating', None)
        min_rating = self.request.query_params.get('min_rating', None)
        max_rating = self.request.query_params.get('max_rating', None)
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        
        # Apply filters if parameters are provided
        if restaurant:
            queryset = queryset.filter(restaurant__id=restaurant)
        
        if user:
            queryset = queryset.filter(user__id=user)
        
        if rating:
            try:
                r = int(rating)
                queryset = queryset.filter(rating=r)
            except ValueError:
                pass
                
        if min_rating:
            try:
                min_r = int(min_rating)
                queryset = queryset.filter(rating__gte=min_r)
            except ValueError:
                pass
                
        if max_rating:
            try:
                max_r = int(max_rating)
                queryset = queryset.filter(rating__lte=max_r)
            except ValueError:
                pass
                
        if date_from:
            try:
                queryset = queryset.filter(created_at__gte=date_from)
            except (ValueError, TypeError):
                pass
                
        if date_to:
            try:
                queryset = queryset.filter(created_at__lte=date_to)
            except (ValueError, TypeError):
                pass
        
        return queryset

    def perform_create(self, serializer):
        """Set the current user as the user creating the review."""
        serializer.save(user=self.request.user)
