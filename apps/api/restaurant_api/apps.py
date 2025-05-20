"""
Django application configuration for the Restaurant API.
"""

from django.apps import AppConfig


class RestaurantApiConfig(AppConfig):
    """Configuration for the Restaurant API application."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant_api'
    verbose_name = 'Restaurant Hub API'
    
    def ready(self):
        """
        Perform initialization when Django starts.
        This is a good place to initialize Prisma.
        """
        # Import signals to register them
        import restaurant_api.signals  # noqa
