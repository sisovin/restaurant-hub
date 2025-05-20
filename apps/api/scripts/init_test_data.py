"""
Script to initialize test data for the Restaurant Hub API.
"""

import os
import sys
import random
import string
import json
import datetime
import uuid
from decimal import Decimal
from pathlib import Path
from django.utils import timezone

# Add the parent directory to the Python path
base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Import Django modules
import django
django.setup()

# Now we can import Django models
from restaurant_api.models import (
    User, Restaurant, RestaurantImage, Menu, MenuCategory, 
    MenuItem, Table, Reservation, Order, OrderItem, Review,
    UserRole, PriceRange, TableLocation, ReservationStatus,
    OrderType, OrderStatus, PaymentMethod, PaymentStatus
)


def random_string(length=10):
    """Generate a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def random_phone():
    """Generate a random phone number."""
    return f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"


def random_date(start_date, end_date=None):
    """Generate a random date between start_date and end_date."""
    if end_date is None:
        end_date = timezone.now()
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)


def random_time():
    """Generate a random time between 9 AM and 10 PM."""
    hour = random.randint(9, 22)
    minute = random.choice([0, 15, 30, 45])
    return datetime.time(hour, minute)


def create_users(count=10):
    """Create random users."""
    print(f"Creating {count} users...")
    
    # Create one of each role
    users = []
    
    # Admin user (only if one doesn't exist)
    if not User.objects.filter(role=UserRole.ADMIN).exists():
        admin = User.objects.create(
            id=str(uuid.uuid4()),
            email="admin@restauranthub.com",
            first_name="Admin",
            last_name="User",
            phone_number=random_phone(),
            role=UserRole.ADMIN,
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        admin.set_password("admin123")
        admin.save()
        users.append(admin)
        print(f"  - Created admin user: {admin.email}")
    
    # Restaurant owner
    owner = User.objects.create(
        id=str(uuid.uuid4()),
        email="owner@restauranthub.com",
        first_name="Restaurant",
        last_name="Owner",
        phone_number=random_phone(),
        role=UserRole.RESTAURANT_OWNER,
        is_active=True,
    )
    owner.set_password("owner123")
    owner.save()
    users.append(owner)
    print(f"  - Created restaurant owner: {owner.email}")
    
    # Staff user
    staff = User.objects.create(
        id=str(uuid.uuid4()),
        email="staff@restauranthub.com",
        first_name="Staff",
        last_name="User",
        phone_number=random_phone(),
        role=UserRole.STAFF,
        is_active=True,
        is_staff=True,
    )
    staff.set_password("staff123")
    staff.save()
    users.append(staff)
    print(f"  - Created staff user: {staff.email}")
    
    # Regular users
    for i in range(count - 3):
        user = User.objects.create(
            id=str(uuid.uuid4()),
            email=f"user{i+1}@example.com",
            first_name=f"User{i+1}",
            last_name="Test",
            phone_number=random_phone(),
            role=UserRole.USER,
            is_active=True,
        )
        user.set_password("user123")
        user.save()
        users.append(user)
    
    print(f"✅ Created {len(users)} users")
    return users


def create_restaurants(owners, count=5):
    """Create random restaurants."""
    print(f"Creating {count} restaurants...")
    
    restaurants = []
    cuisines = [
        "Italian", "Chinese", "Mexican", "Indian", "Japanese", 
        "Thai", "French", "American", "Mediterranean", "Greek"
    ]
    
    cities = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
    ]
    
    for i in range(count):
        owner = random.choice(owners)
        
        # Generate opening hours
        opening_hours = {}
        for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
            opening_hours[day] = {"open": "09:00", "close": "22:00"}
        for day in ["saturday", "sunday"]:
            opening_hours[day] = {"open": "10:00", "close": "23:00"}
        
        restaurant = Restaurant.objects.create(
            id=str(uuid.uuid4()),
            name=f"{random.choice(['The', 'La', 'El', 'Big', 'Little', 'Golden'])} {random.choice(cuisines)} {random.choice(['Restaurant', 'Bistro', 'Cafe', 'Diner', 'Grill'])}",
            description=f"A {random.choice(['cozy', 'stylish', 'rustic', 'elegant', 'modern'])} {random.choice(cuisines)} restaurant with {random.choice(['authentic', 'traditional', 'innovative', 'fusion', 'homestyle'])} cuisine.",
            address=f"{random.randint(100, 999)} {random.choice(['Main', 'Oak', 'Maple', 'Pine', 'Cedar'])} {random.choice(['St', 'Ave', 'Blvd', 'Rd', 'Ln'])}",
            city=random.choice(cities),
            state=random.choice(["NY", "CA", "TX", "IL", "PA"]),
            country="USA",
            postal_code=f"{random.randint(10000, 99999)}",
            phone_number=random_phone(),
            email=f"info@{random_string(8).lower()}.com",
            website=f"https://www.{random_string(8).lower()}.com",
            opening_hours=opening_hours,
            cuisine_type=[random.choice(cuisines), random.choice(cuisines)],
            price_range=random.choice(list(PriceRange)),
            is_active=True,
            is_verified=random.choice([True, False]),
            owner=owner,
        )
        restaurants.append(restaurant)
    
    print(f"✅ Created {len(restaurants)} restaurants")
    return restaurants


def create_restaurant_images(restaurants, count_per_restaurant=3):
    """Create random restaurant images."""
    print(f"Creating restaurant images ({count_per_restaurant} per restaurant)...")
    
    images = []
    image_urls = [
        "https://source.unsplash.com/random/800x600/?restaurant",
        "https://source.unsplash.com/random/800x600/?cafe",
        "https://source.unsplash.com/random/800x600/?dining",
        "https://source.unsplash.com/random/800x600/?food",
        "https://source.unsplash.com/random/800x600/?interior",
    ]
    
    for restaurant in restaurants:
        for i in range(count_per_restaurant):
            is_primary = (i == 0)  # First image is primary
            image = RestaurantImage.objects.create(
                id=str(uuid.uuid4()),
                restaurant=restaurant,
                image_url=random.choice(image_urls),
                alt_text=f"Image of {restaurant.name}",
                is_primary=is_primary,
            )
            images.append(image)
    
    print(f"✅ Created {len(images)} restaurant images")
    return images


def create_menus(restaurants, count_per_restaurant=1):
    """Create random menus."""
    print(f"Creating menus ({count_per_restaurant} per restaurant)...")
    
    menus = []
    for restaurant in restaurants:
        for i in range(count_per_restaurant):
            menu = Menu.objects.create(
                id=str(uuid.uuid4()),
                restaurant=restaurant,
                name=f"{restaurant.name} {random.choice(['Main', 'Lunch', 'Dinner', 'Special'])} Menu",
                description=f"Our {random.choice(['signature', 'seasonal', 'chef\\'s selection', 'recommended', 'popular'])} menu featuring {random.choice(['fresh', 'local', 'organic', 'handcrafted', 'gourmet'])} dishes.",
                is_active=True,
            )
            menus.append(menu)
    
    print(f"✅ Created {len(menus)} menus")
    return menus


def create_menu_categories(menus, count_per_menu=4):
    """Create random menu categories."""
    print(f"Creating menu categories ({count_per_menu} per menu)...")
    
    categories = []
    category_names = [
        "Appetizers", "Soups", "Salads", "Main Courses", 
        "Pasta", "Seafood", "Vegetarian", "Desserts", 
        "Beverages", "Sides", "Specials", "Kids Menu"
    ]
    
    for menu in menus:
        # Shuffle the category names to get a random selection
        random.shuffle(category_names)
        selected_categories = category_names[:count_per_menu]
        
        for i, name in enumerate(selected_categories):
            category = MenuCategory.objects.create(
                id=str(uuid.uuid4()),
                menu=menu,
                name=name,
                description=f"Our {random.choice(['delicious', 'fresh', 'signature', 'house', 'classic'])} {name.lower()}.",
                display_order=i,
                is_active=True,
            )
            categories.append(category)
    
    print(f"✅ Created {len(categories)} menu categories")
    return categories


def create_menu_items(categories, count_per_category=5):
    """Create random menu items."""
    print(f"Creating menu items ({count_per_category} per category)...")
    
    items = []
    
    # Define some common menu items by category
    menu_items_by_category = {
        "Appetizers": [
            {"name": "Bruschetta", "price": "8.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Mozzarella Sticks", "price": "9.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Calamari", "price": "12.99", "veg": False, "vegan": False, "gf": False},
            {"name": "Nachos", "price": "10.99", "veg": True, "vegan": False, "gf": True},
            {"name": "Buffalo Wings", "price": "11.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Spinach Artichoke Dip", "price": "9.99", "veg": True, "vegan": False, "gf": False},
        ],
        "Soups": [
            {"name": "Tomato Basil Soup", "price": "6.99", "veg": True, "vegan": False, "gf": True},
            {"name": "Chicken Noodle Soup", "price": "7.99", "veg": False, "vegan": False, "gf": False},
            {"name": "Minestrone", "price": "7.99", "veg": True, "vegan": True, "gf": False},
            {"name": "Clam Chowder", "price": "8.99", "veg": False, "vegan": False, "gf": False},
            {"name": "French Onion Soup", "price": "7.99", "veg": True, "vegan": False, "gf": False},
        ],
        "Salads": [
            {"name": "Caesar Salad", "price": "10.99", "veg": True, "vegan": False, "gf": True},
            {"name": "Greek Salad", "price": "11.99", "veg": True, "vegan": False, "gf": True},
            {"name": "Cobb Salad", "price": "12.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Spinach Salad", "price": "10.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Caprese Salad", "price": "11.99", "veg": True, "vegan": False, "gf": True},
        ],
        "Main Courses": [
            {"name": "Grilled Salmon", "price": "18.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Ribeye Steak", "price": "24.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Chicken Parmesan", "price": "16.99", "veg": False, "vegan": False, "gf": False},
            {"name": "Beef Bourguignon", "price": "19.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Eggplant Parmesan", "price": "15.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Grilled Chicken", "price": "16.99", "veg": False, "vegan": False, "gf": True},
        ],
        "Pasta": [
            {"name": "Spaghetti Bolognese", "price": "14.99", "veg": False, "vegan": False, "gf": False},
            {"name": "Fettuccine Alfredo", "price": "13.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Lasagna", "price": "15.99", "veg": False, "vegan": False, "gf": False},
            {"name": "Penne alla Vodka", "price": "14.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Linguine with Clams", "price": "17.99", "veg": False, "vegan": False, "gf": False},
        ],
        "Seafood": [
            {"name": "Grilled Shrimp", "price": "19.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Lobster Tail", "price": "29.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Fish and Chips", "price": "16.99", "veg": False, "vegan": False, "gf": False},
            {"name": "Seafood Paella", "price": "22.99", "veg": False, "vegan": False, "gf": True},
            {"name": "Crab Cakes", "price": "18.99", "veg": False, "vegan": False, "gf": False},
        ],
        "Vegetarian": [
            {"name": "Vegetable Stir-Fry", "price": "14.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Mushroom Risotto", "price": "15.99", "veg": True, "vegan": False, "gf": True},
            {"name": "Vegetable Curry", "price": "14.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Stuffed Bell Peppers", "price": "13.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Quinoa Bowl", "price": "12.99", "veg": True, "vegan": True, "gf": True},
        ],
        "Desserts": [
            {"name": "Tiramisu", "price": "7.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Chocolate Cake", "price": "6.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Cheesecake", "price": "7.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Apple Pie", "price": "6.99", "veg": True, "vegan": False, "gf": False},
            {"name": "Crème Brûlée", "price": "8.99", "veg": True, "vegan": False, "gf": True},
        ],
        "Beverages": [
            {"name": "Soft Drink", "price": "2.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Iced Tea", "price": "2.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Coffee", "price": "3.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Lemonade", "price": "3.99", "veg": True, "vegan": True, "gf": True},
            {"name": "Sparkling Water", "price": "2.99", "veg": True, "vegan": True, "gf": True},
        ],
    }
    
    for category in categories:
        # Get menu items for this category or use generic items
        category_items = menu_items_by_category.get(
            category.name, 
            [{"name": f"Item {i}", "price": f"{random.randint(5, 25)}.99", "veg": random.choice([True, False]), "vegan": random.choice([True, False]), "gf": random.choice([True, False])} for i in range(count_per_category)]
        )
        
        # Use all available items or up to count_per_category
        selected_items = category_items[:count_per_category]
        
        # If we need more items, add some generic ones
        while len(selected_items) < count_per_category:
            i = len(selected_items) + 1
            selected_items.append({"name": f"Item {i}", "price": f"{random.randint(5, 25)}.99", "veg": random.choice([True, False]), "vegan": random.choice([True, False]), "gf": random.choice([True, False])})
        
        for i, item_data in enumerate(selected_items):
            # Create the menu item
            item = MenuItem.objects.create(
                id=str(uuid.uuid4()),
                category=category,
                name=item_data["name"],
                description=f"Our {random.choice(['delicious', 'homemade', 'chef\\'s special', 'signature', 'fresh'])} {item_data['name'].lower()}.",
                price=Decimal(item_data["price"]),
                image_url=f"https://source.unsplash.com/random/300x200/?food,{item_data['name'].replace(' ', '')}",
                ingredients=f"Fresh {random.choice(['local', 'organic', 'seasonal', 'premium', 'imported'])} ingredients.",
                allergens=random.sample(["Gluten", "Dairy", "Nuts", "Soy", "Shellfish", "Eggs"], k=random.randint(0, 3)),
                is_vegetarian=item_data["veg"],
                is_vegan=item_data["vegan"],
                is_gluten_free=item_data["gf"],
                spicy_level=random.randint(0, 5),
                is_available=True,
                display_order=i,
            )
            items.append(item)
    
    print(f"✅ Created {len(items)} menu items")
    return items


def create_tables(restaurants, count_per_restaurant=8):
    """Create random tables."""
    print(f"Creating tables ({count_per_restaurant} per restaurant)...")
    
    tables = []
    for restaurant in restaurants:
        for i in range(count_per_restaurant):
            # Determine table capacity and location
            if i < 2:
                # First tables are for 2 people
                capacity = 2
                location = TableLocation.INDOOR
            elif i < 4:
                # Next tables are for 4 people
                capacity = 4
                location = TableLocation.INDOOR
            elif i < 6:
                # Next tables are for 6 people
                capacity = 6
                location = random.choice([TableLocation.INDOOR, TableLocation.OUTDOOR])
            else:
                # Remaining tables have random capacity and location
                capacity = random.choice([2, 4, 6, 8])
                location = random.choice(list(TableLocation))
            
            table = Table.objects.create(
                id=str(uuid.uuid4()),
                restaurant=restaurant,
                table_number=f"T{i+1}",
                capacity=capacity,
                is_available=random.choice([True, True, True, False]),  # 75% chance of being available
                location=location,
            )
            tables.append(table)
    
    print(f"✅ Created {len(tables)} tables")
    return tables


def create_reservations(users, restaurants, tables, count=20):
    """Create random reservations."""
    print(f"Creating {count} reservations...")
    
    reservations = []
    
    # Generate future dates for reservations
    today = timezone.now().date()
    future_dates = [today + datetime.timedelta(days=i) for i in range(1, 31)]
    
    for _ in range(count):
        # Select a random user, restaurant, and table
        user = random.choice(users)
        restaurant = random.choice(restaurants)
        
        # Get tables for this restaurant
        restaurant_tables = [table for table in tables if table.restaurant == restaurant]
        if not restaurant_tables:
            continue
        
        table = random.choice(restaurant_tables)
        
        # Generate random reservation date and time
        reservation_date = random.choice(future_dates)
        start_hour = random.randint(11, 20)  # 11 AM to 8 PM
        start_minute = random.choice([0, 15, 30, 45])
        start_time = datetime.datetime.combine(reservation_date, datetime.time(start_hour, start_minute))
        # End time is 1.5 hours after start time
        end_time = start_time + datetime.timedelta(hours=1, minutes=30)
        
        # Generate random guest count (up to table capacity)
        guest_count = random.randint(1, table.capacity)
        
        # Determine reservation status
        status = random.choices(
            list(ReservationStatus),
            weights=[70, 10, 10, 5, 5],  # Weights for each status
            k=1
        )[0]
        
        # Create the reservation
        reservation = Reservation.objects.create(
            id=str(uuid.uuid4()),
            user=user,
            restaurant=restaurant,
            table=table,
            reservation_date=reservation_date,
            start_time=start_time,
            end_time=end_time,
            guest_count=guest_count,
            special_requests=random.choice([None, "Window seat please", "Anniversary celebration", "Birthday celebration", "No spicy food", "Allergic to nuts"]),
            status=status,
        )
        
        # If cancelled, set cancelled_at
        if status == ReservationStatus.CANCELLED:
            reservation.cancelled_at = timezone.now() - datetime.timedelta(days=random.randint(1, 5))
            reservation.save()
        
        reservations.append(reservation)
    
    print(f"✅ Created {len(reservations)} reservations")
    return reservations


def create_orders(users, restaurants, menu_items, count=30):
    """Create random orders."""
    print(f"Creating {count} orders...")
    
    orders = []
    
    for i in range(count):
        # Select a random user and restaurant
        user = random.choice(users)
        restaurant = random.choice(restaurants)
        
        # Generate a random order number
        order_number = f"ORD-{random.randint(10000, 99999)}"
        
        # Determine order type and status
        order_type = random.choice(list(OrderType))
        
        # The status depends partly on the order date
        order_placed_date = random.choice([
            timezone.now() - datetime.timedelta(days=random.randint(1, 30)),  # Past order
            timezone.now(),  # Current order
            timezone.now() - datetime.timedelta(hours=random.randint(1, 12))  # Recent order
        ])
        
        # Newer orders are more likely to be in earlier stages
        if (timezone.now() - order_placed_date).days > 7:
            # Older orders are completed or cancelled
            status = random.choice([OrderStatus.COMPLETED, OrderStatus.CANCELLED])
        elif (timezone.now() - order_placed_date).days > 1:
            # Orders from yesterday or earlier are likely completed
            status = random.choice([OrderStatus.COMPLETED, OrderStatus.DELIVERED, OrderStatus.PICKED_UP])
        else:
            # Recent orders have various statuses
            status = random.choice(list(OrderStatus))
        
        # Set payment method and status
        payment_method = random.choice(list(PaymentMethod))
        
        # Payment status depends on order status
        if status in [OrderStatus.COMPLETED, OrderStatus.DELIVERED, OrderStatus.PICKED_UP]:
            payment_status = PaymentStatus.PAID
        elif status == OrderStatus.CANCELLED:
            payment_status = random.choice([PaymentStatus.REFUNDED, PaymentStatus.FAILED])
        else:
            payment_status = random.choice([PaymentStatus.PENDING, PaymentStatus.PAID])
        
        # Set delivery address for delivery orders
        delivery_address = None
        delivery_fee = None
        if order_type == OrderType.DELIVERY:
            delivery_address = f"{random.randint(100, 999)} {random.choice(['Main', 'Oak', 'Maple', 'Pine', 'Cedar'])} {random.choice(['St', 'Ave', 'Blvd', 'Rd', 'Ln'])}, {restaurant.city}, {restaurant.state} {restaurant.postal_code}"
            delivery_fee = Decimal(f"{random.randint(3, 8)}.{random.randint(0, 99):02d}")
        
        # Set completed time for completed orders
        order_completed_at = None
        if status in [OrderStatus.COMPLETED, OrderStatus.DELIVERED, OrderStatus.PICKED_UP]:
            # Completed 30 minutes to 2 hours after being placed
            order_completed_at = order_placed_date + datetime.timedelta(minutes=random.randint(30, 120))
        
        # Create the order with initial values
        order = Order.objects.create(
            id=str(uuid.uuid4()),
            user=user,
            restaurant=restaurant,
            order_number=order_number,
            order_type=order_type,
            status=status,
            total_amount=Decimal("0.00"),  # Will be updated after adding items
            tax_amount=Decimal("0.00"),    # Will be updated after adding items
            tip_amount=Decimal(f"{random.randint(0, 10)}.{random.randint(0, 99):02d}") if random.choice([True, False]) else None,
            discount_amount=Decimal(f"{random.randint(0, 15)}.{random.randint(0, 99):02d}") if random.choice([True, False, False]) else None,  # 1/3 chance of discount
            delivery_address=delivery_address,
            delivery_fee=delivery_fee,
            payment_method=payment_method,
            payment_status=payment_status,
            special_instructions=random.choice([None, "Ring doorbell", "Call upon arrival", "Extra napkins", "No utensils", "No contact delivery"]),
            estimated_delivery_time=order_placed_date + datetime.timedelta(minutes=random.randint(30, 60)) if order_type == OrderType.DELIVERY else None,
            order_placed_at=order_placed_date,
            order_completed_at=order_completed_at,
        )
        
        # Get menu items for this restaurant
        restaurant_categories = MenuCategory.objects.filter(menu__restaurant=restaurant)
        restaurant_items = [item for item in menu_items if item.category in restaurant_categories]
        
        if restaurant_items:
            # Add 1-5 items to the order
            num_items = random.randint(1, 5)
            selected_items = random.sample(restaurant_items, min(num_items, len(restaurant_items)))
            
            subtotal = Decimal("0.00")
            
            for item in selected_items:
                # Create order item
                quantity = random.randint(1, 3)
                unit_price = item.price
                total_price = unit_price * quantity
                
                OrderItem.objects.create(
                    id=str(uuid.uuid4()),
                    order=order,
                    menu_item=item,
                    quantity=quantity,
                    unit_price=unit_price,
                    total_price=total_price,
                    special_instructions=random.choice([None, "No onions", "Extra spicy", "Light sauce", "Well done"]),
                )
                
                subtotal += total_price
            
            # Calculate tax, total, etc.
            tax_rate = Decimal("0.08")  # 8% tax
            tax_amount = subtotal * tax_rate
            
            # Add delivery fee if applicable
            if delivery_fee:
                subtotal += delivery_fee
            
            # Apply discount if applicable
            discount = order.discount_amount or Decimal("0.00")
            
            # Calculate final total
            total_amount = subtotal + tax_amount - discount
            
            # Update the order with calculated amounts
            order.total_amount = total_amount
            order.tax_amount = tax_amount
            order.save()
        
        orders.append(order)
    
    print(f"✅ Created {len(orders)} orders")
    return orders


def create_reviews(users, restaurants, count=40):
    """Create random reviews."""
    print(f"Creating {count} reviews...")
    
    reviews = []
    
    for _ in range(count):
        # Select a random user and restaurant
        user = random.choice(users)
        restaurant = random.choice(restaurants)
        
        # Generate a random rating (1-5 stars)
        rating = random.randint(1, 5)
        
        # Generate a comment based on rating
        comments_by_rating = {
            1: [
                "Terrible experience. Food was cold and service was slow.",
                "Would not recommend. Very disappointing.",
                "Not worth the money. Won't be returning.",
            ],
            2: [
                "Below average. Several issues with our meal.",
                "Service was okay but food was mediocre.",
                "Expected better for the price.",
            ],
            3: [
                "Average experience. Nothing special.",
                "Food was decent but not memorable.",
                "Okay for a casual meal but nothing extraordinary.",
            ],
            4: [
                "Very good food and service. Would visit again.",
                "Enjoyed our meal. Only minor issues.",
                "Great atmosphere and tasty food.",
            ],
            5: [
                "Outstanding experience! Definitely coming back.",
                "Best meal I've had in a long time. Highly recommended!",
                "Exceptional service and delicious food. A new favorite!",
            ]
        }
        
        comment = random.choice(comments_by_rating[rating])
        
        # Create the review
        review = Review.objects.create(
            id=str(uuid.uuid4()),
            user=user,
            restaurant=restaurant,
            rating=rating,
            comment=comment,
            is_published=True,
        )
        
        reviews.append(review)
    
    # After creating reviews, update restaurant ratings
    for restaurant in restaurants:
        restaurant_reviews = Review.objects.filter(restaurant=restaurant, is_published=True)
        if restaurant_reviews.exists():
            avg_rating = sum(review.rating for review in restaurant_reviews) / restaurant_reviews.count()
            restaurant.rating = round(avg_rating, 1)
            restaurant.save()
    
    print(f"✅ Created {len(reviews)} reviews")
    print("✅ Updated restaurant ratings")
    return reviews


def main():
    """Main function to initialize test data."""
    print("Initializing test data for the Restaurant Hub API...")
    
    # Check if data already exists
    if User.objects.exists():
        print("⚠️ Data already exists. Skipping initialization.")
        return
    
    # Create test data
    users = create_users(count=10)
    owners = [user for user in users if user.role == UserRole.RESTAURANT_OWNER]
    if not owners:
        owners = [users[0]]  # Use the first user as owner if no owners found
    
    restaurants = create_restaurants(owners, count=5)
    create_restaurant_images(restaurants, count_per_restaurant=3)
    menus = create_menus(restaurants, count_per_restaurant=1)
    categories = create_menu_categories(menus, count_per_menu=4)
    menu_items = create_menu_items(categories, count_per_category=5)
    tables = create_tables(restaurants, count_per_restaurant=8)
    create_reservations(users, restaurants, tables, count=20)
    create_orders(users, restaurants, menu_items, count=30)
    create_reviews(users, restaurants, count=40)
    
    print("✅ Test data initialization completed successfully")


if __name__ == "__main__":
    main()
