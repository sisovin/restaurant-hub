"""
Management command to create sample data for the Restaurant Hub API.
"""

import random
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model
from restaurant_api.models import (
    Restaurant, RestaurantImage, Menu, MenuCategory, MenuItem,
    Table, Review, User, UserRole, PriceRange, TableLocation
)

User = get_user_model()

CUISINES = [
    'Italian', 'Mexican', 'Chinese', 'Japanese', 'Indian', 
    'Thai', 'American', 'French', 'Mediterranean', 'Greek'
]

RESTAURANT_NAMES = [
    'The Hungry Bear', 'Olive Garden', 'Spice Palace', 'Golden Dragon',
    'Sakura Sushi', 'Taj Mahal', 'Thai Orchid', 'Burger Heaven',
    'Le Petit Bistro', 'Mediterranean Delight', 'Greek Islands'
]

MENU_NAMES = [
    'Breakfast', 'Lunch', 'Dinner', 'Brunch', 'Happy Hour',
    'Kids Menu', 'Desserts', 'Drinks', 'Specials', 'Seasonal'
]

CATEGORY_NAMES = [
    'Appetizers', 'Soups', 'Salads', 'Main Courses', 'Desserts',
    'Drinks', 'Sides', 'Specials', 'Kids Menu', 'Vegetarian', 'Vegan'
]

MENU_ITEMS = {
    'Appetizers': [
        ('Mozzarella Sticks', 'Deep-fried mozzarella cheese sticks served with marinara sauce', 7.99),
        ('Nachos', 'Tortilla chips topped with cheese, jalapeños, sour cream, and salsa', 8.99),
        ('Bruschetta', 'Toasted bread topped with tomatoes, garlic, basil, and olive oil', 6.99),
        ('Chicken Wings', 'Crispy chicken wings with your choice of sauce', 9.99),
        ('Calamari', 'Fried squid rings served with tartar sauce', 10.99),
    ],
    'Soups': [
        ('Tomato Soup', 'Creamy tomato soup with basil and croutons', 4.99),
        ('Chicken Noodle Soup', 'Classic chicken soup with noodles and vegetables', 5.99),
        ('Minestrone', 'Italian vegetable soup with pasta and beans', 5.99),
        ('Clam Chowder', 'Creamy soup with clams, potatoes, and bacon', 6.99),
        ('Mushroom Soup', 'Creamy soup with assorted mushrooms', 5.99),
    ],
    'Salads': [
        ('Caesar Salad', 'Romaine lettuce with Caesar dressing, croutons, and parmesan', 8.99),
        ('Greek Salad', 'Mixed greens with feta, olives, tomatoes, and cucumbers', 9.99),
        ('Cobb Salad', 'Mixed greens with chicken, bacon, egg, avocado, and blue cheese', 11.99),
        ('Garden Salad', 'Mixed greens with assorted vegetables', 7.99),
        ('Spinach Salad', 'Spinach with strawberries, walnuts, and goat cheese', 10.99),
    ],
    'Main Courses': [
        ('Spaghetti Bolognese', 'Spaghetti with beef and tomato sauce', 13.99),
        ('Chicken Alfredo', 'Fettuccine with grilled chicken and Alfredo sauce', 14.99),
        ('Beef Burger', 'Beef patty with lettuce, tomato, onion, and cheese', 12.99),
        ('Grilled Salmon', 'Grilled salmon fillet with seasonal vegetables', 17.99),
        ('Chicken Parmesan', 'Breaded chicken with marinara sauce and mozzarella', 15.99),
        ('Vegetable Stir Fry', 'Assorted vegetables stir-fried with tofu and rice', 12.99),
        ('New York Strip Steak', '12oz steak with mashed potatoes and vegetables', 23.99),
        ('Fish and Chips', 'Battered cod with french fries and tartar sauce', 14.99),
        ('Cheese Pizza', 'Classic pizza with tomato sauce and mozzarella', 11.99),
        ('Chicken Curry', 'Chicken curry with rice and naan bread', 15.99),
    ],
    'Desserts': [
        ('Chocolate Cake', 'Rich chocolate cake with chocolate ganache', 6.99),
        ('Cheesecake', 'New York style cheesecake with strawberry topping', 7.99),
        ('Apple Pie', 'Warm apple pie with vanilla ice cream', 6.99),
        ('Tiramisu', 'Italian coffee-flavored dessert with mascarpone', 8.99),
        ('Ice Cream Sundae', 'Vanilla ice cream with chocolate sauce and whipped cream', 5.99),
    ],
    'Drinks': [
        ('Soda', 'Cola, lemon-lime, or root beer', 2.99),
        ('Iced Tea', 'Sweetened or unsweetened iced tea', 2.99),
        ('Coffee', 'Regular or decaf coffee', 2.99),
        ('Lemonade', 'Fresh-squeezed lemonade', 3.99),
        ('Milkshake', 'Chocolate, vanilla, or strawberry milkshake', 4.99),
    ],
}

class Command(BaseCommand):
    """Command to create sample data for the Restaurant Hub API."""
    
    help = 'Creates sample data for the Restaurant Hub API'
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Handle the command."""
        self.stdout.write('Creating sample data...')
        
        # Clear existing data
        self.clear_data()
        
        # Create users
        self.create_users()
        
        # Create restaurants
        self.create_restaurants()
        
        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))
    
    def clear_data(self):
        """Clear existing data."""
        self.stdout.write('Clearing existing data...')
        
        Review.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuCategory.objects.all().delete()
        Menu.objects.all().delete()
        Table.objects.all().delete()
        RestaurantImage.objects.all().delete()
        Restaurant.objects.all().delete()
        
        # Don't delete superuser
        User.objects.filter(is_superuser=False).delete()
    
    def create_users(self):
        """Create sample users."""
        self.stdout.write('Creating users...')
        
        # Create admin user if it doesn't exist
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create_superuser(
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
        
        # Create regular users
        for i in range(5):
            User.objects.create_user(
                email=f'user{i+1}@example.com',
                password=f'password{i+1}',
                first_name=f'User{i+1}',
                last_name='Test',
                role=UserRole.USER
            )
        
        # Create restaurant owners
        for i in range(3):
            User.objects.create_user(
                email=f'owner{i+1}@example.com',
                password=f'password{i+1}',
                first_name=f'Owner{i+1}',
                last_name='Test',
                role=UserRole.OWNER
            )
    
    def create_restaurants(self):
        """Create sample restaurants with related data."""
        self.stdout.write('Creating restaurants...')
        
        owners = User.objects.filter(role=UserRole.OWNER)
        users = User.objects.filter(role=UserRole.USER)
        
        for i, name in enumerate(RESTAURANT_NAMES):
            # Assign an owner (cycle through available owners)
            owner = owners[i % len(owners)]
            
            # Create restaurant
            restaurant = Restaurant.objects.create(
                name=name,
                description=f'A great {CUISINES[i % len(CUISINES)]} restaurant',
                address=f'{123 + i} Main St',
                city='Anytown',
                state='CA',
                country='USA',
                postal_code=f'9000{i}',
                phone_number=f'555-555-{1000 + i}',
                email=f'info@{name.lower().replace(" ", "")}.com',
                website=f'https://www.{name.lower().replace(" ", "")}.com',
                cuisine_type=CUISINES[i % len(CUISINES)],
                price_range=random.choice(list(PriceRange.choices))[0],
                owner=owner,
                rating=round(random.uniform(3.0, 5.0), 1),
            )
            
            # Create restaurant images
            RestaurantImage.objects.create(
                restaurant=restaurant,
                image_url=f'https://via.placeholder.com/800x600.png?text={name.replace(" ", "+")}',
                alt_text=f'{name} exterior',
                is_primary=True
            )
            
            RestaurantImage.objects.create(
                restaurant=restaurant,
                image_url=f'https://via.placeholder.com/800x600.png?text={name.replace(" ", "+")}-Interior',
                alt_text=f'{name} interior',
                is_primary=False
            )
            
            # Create menus
            for j, menu_name in enumerate(MENU_NAMES[:3]):  # Create 3 menus per restaurant
                menu = Menu.objects.create(
                    restaurant=restaurant,
                    name=menu_name,
                    description=f'{menu_name} menu at {restaurant.name}'
                )
                
                # Create menu categories
                for k, category_name in enumerate(CATEGORY_NAMES[:5]):  # Create 5 categories per menu
                    category = MenuCategory.objects.create(
                        menu=menu,
                        name=category_name,
                        description=f'{category_name} at {restaurant.name}',
                        display_order=k
                    )
                    
                    # Create menu items
                    if category_name in MENU_ITEMS:
                        for l, (item_name, item_desc, price) in enumerate(MENU_ITEMS[category_name]):
                            MenuItem.objects.create(
                                category=category,
                                name=item_name,
                                description=item_desc,
                                price=price,
                                image_url=f'https://via.placeholder.com/300x200.png?text={item_name.replace(" ", "+")}',
                                ingredients='Various ingredients',
                                allergens='May contain allergens',
                                is_vegetarian=random.choice([True, False]),
                                is_vegan=random.choice([True, False]),
                                is_gluten_free=random.choice([True, False]),
                                display_order=l
                            )
            
            # Create tables
            for j in range(5):  # 5 tables per restaurant
                Table.objects.create(
                    restaurant=restaurant,
                    table_number=f'T{j+1}',
                    capacity=random.choice([2, 4, 6, 8]),
                    location=random.choice(list(TableLocation.choices))[0]
                )
              # Create reviews - ensuring no duplicates
            used_users = set()
            for j in range(min(3, len(users))):  # 3 reviews per restaurant or fewer if not enough users
                # Find a user who hasn't reviewed this restaurant yet
                available_users = [u for u in users if u.id not in used_users]
                if not available_users:
                    break
                    
                user = random.choice(available_users)
                used_users.add(user.id)
                
                rating = random.randint(3, 5)
                Review.objects.create(
                    user=user,
                    restaurant=restaurant,
                    rating=rating,
                    comment=f'{"Great" if rating >= 4 else "Good"} restaurant. {"Highly recommended!" if rating == 5 else ""}'
                )
