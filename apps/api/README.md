# Restaurant Hub API

A comprehensive Django REST API for a restaurant management system, featuring a self-delete design with PostgreSQL.

## 🚀 Features

- **Complete Restaurant Management**: Manage restaurants, menus, orders, reservations, and reviews
- **Soft Delete Design**: All models implement a "soft delete" pattern for data preservation
- **Prisma Integration**: Uses Prisma ORM with Django for powerful database access
- **RESTful API**: Comprehensive REST endpoints using Django REST Framework
- **Authentication**: JWT-based authentication system
- **Admin Interface**: Customized Django admin for easy management

## � Models

- **User**: Authentication and user management
- **Restaurant**: Restaurant details with location, hours, and cuisine types
- **Menu/MenuCategory/MenuItem**: Full menu structure with categories and items
- **Table/Reservation**: Table management and reservation system
- **Order/OrderItem**: Comprehensive order management
- **Review**: Customer review system with ratings

## 🔧 Technology Stack

- **Framework**: Django 4.2+ / Django REST Framework
- **Database**: PostgreSQL
- **ORM**: Prisma + Django ORM
- **Authentication**: JWT (JSON Web Tokens)
- **Documentation**: Auto-generated API documentation

## 💻 Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Node.js 16+ (for Prisma CLI)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd restaurant-hub/apps/api
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   npm install -g prisma  # Install Prisma CLI globally
   ```

4. **Configure the database**
   - Create a PostgreSQL database
   - Update `prisma/.env` with your database connection string:
     ```
     DATABASE_URL="postgresql://user:password@localhost:5432/restaurant_hub"
     ```

5. **Initialize Prisma**
   ```bash
   python scripts/init_prisma.py
   ```

6. **Set up the database**
   ```bash
   python scripts/setup_db.py
   ```

7. **Load test data (optional)**
   ```bash
   python scripts/init_test_data.py
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 🔑 API Access

The API will be available at `http://localhost:8000/api/`

### Authentication

Use JWT authentication:
```
POST /api/token/
{
  "email": "user@example.com",
  "password": "password"
}
```

Response:
```json
{
  "access": "your-access-token",
  "refresh": "your-refresh-token"
}
```

Include the token in your requests:
```
Authorization: Bearer your-access-token
```

## � Available Endpoints

- `/api/users/` - User management
- `/api/restaurants/` - Restaurant operations
- `/api/menus/` - Menu management
- `/api/menu-categories/` - Menu category management
- `/api/menu-items/` - Menu item operations
- `/api/tables/` - Table management
- `/api/reservations/` - Reservation system
- `/api/orders/` - Order processing
- `/api/reviews/` - Customer reviews

## 👩‍💻 Development

### Creating Database Migrations

When changing models:

```bash
prisma migrate dev --name your_migration_name
python manage.py makemigrations
python manage.py migrate
```

### Testing

```bash
python manage.py test
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

