"""
Script to perform database setup and migrations.
"""

import os
import subprocess
import sys
from pathlib import Path


def ensure_database_exists():
    """Ensure the PostgreSQL database exists."""
    print("Checking PostgreSQL database...")
    
    # Get database URL from environment
    base_dir = Path(__file__).resolve().parent.parent
    env_path = os.path.join(base_dir, 'prisma', '.env')
    
    # Load DATABASE_URL from .env file
    database_url = None
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.startswith('DATABASE_URL='):
                    database_url = line.strip().split('=', 1)[1].strip('"\'')
                    break
    
    if not database_url:
        print("❌ DATABASE_URL not found in .env file")
        sys.exit(1)
    
    # Parse the database URL to get the database name
    # Example: postgresql://postgres:password@localhost:5432/restaurant_hub
    try:
        db_name = database_url.split('/')[-1]
        db_host = database_url.split('@')[1].split(':')[0]
        db_port = database_url.split(':')[-2].split('/')[0]
        db_user = database_url.split('://')[1].split(':')[0]
        
        print(f"Database information:")
        print(f"  - Name: {db_name}")
        print(f"  - Host: {db_host}")
        print(f"  - Port: {db_port}")
        print(f"  - User: {db_user}")
        
        # Check if the database exists using psql
        # This command will return 0 if the database exists, non-zero otherwise
        check_cmd = [
            'psql',
            '-h', db_host,
            '-p', db_port,
            '-U', db_user,
            '-lqt'
        ]
        
        print(f"Checking if database '{db_name}' exists...")
        result = subprocess.run(check_cmd, capture_output=True, text=True)
        
        if db_name in result.stdout:
            print(f"✅ Database '{db_name}' exists")
        else:
            print(f"❌ Database '{db_name}' does not exist. Creating...")
            create_cmd = [
                'psql',
                '-h', db_host,
                '-p', db_port,
                '-U', db_user,
                '-c', f"CREATE DATABASE {db_name};"
            ]
            
            subprocess.run(create_cmd, check=True)
            print(f"✅ Database '{db_name}' created successfully")
    
    except (IndexError, subprocess.CalledProcessError) as e:
        print(f"❌ Error checking/creating database: {str(e)}")
        sys.exit(1)


def run_prisma_migrate():
    """Run Prisma migrations."""
    print("Running Prisma migrations...")
    
    # Get the path to the Prisma schema
    base_dir = Path(__file__).resolve().parent.parent
    schema_path = os.path.join(base_dir, 'prisma', 'schema.prisma')
    
    # Check if the schema file exists
    if not os.path.exists(schema_path):
        print(f"❌ Schema file not found at {schema_path}")
        sys.exit(1)
    
    try:
        # Create a migration
        migration_name = "init" if not os.path.exists(os.path.join(base_dir, 'prisma', 'migrations')) else "update"
        print(f"Creating migration '{migration_name}'...")
        
        subprocess.run([
            'prisma', 'migrate', 'dev',
            '--name', migration_name,
            '--schema', schema_path,
            '--skip-generate'
        ], check=True)
        
        print("✅ Prisma migrations applied successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to run Prisma migrations: {str(e)}")
        sys.exit(1)


def run_django_migrations():
    """Run Django migrations."""
    print("Running Django migrations...")
    
    # Get the path to manage.py
    base_dir = Path(__file__).resolve().parent.parent
    manage_path = os.path.join(base_dir, 'manage.py')
    
    # Check if manage.py exists
    if not os.path.exists(manage_path):
        print(f"❌ manage.py not found at {manage_path}")
        sys.exit(1)
    
    try:
        # Run Django migrations
        subprocess.run(['python', manage_path, 'migrate'], check=True)
        print("✅ Django migrations applied successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to run Django migrations")
        sys.exit(1)


def create_superuser():
    """Create a Django superuser."""
    print("Creating a Django superuser...")
    
    # Get the path to manage.py
    base_dir = Path(__file__).resolve().parent.parent
    manage_path = os.path.join(base_dir, 'manage.py')
    
    # Check if manage.py exists
    if not os.path.exists(manage_path):
        print(f"❌ manage.py not found at {manage_path}")
        sys.exit(1)
    
    try:
        # Run the createsuperuser command interactively
        subprocess.run(['python', manage_path, 'createsuperuser'], check=True)
        print("✅ Django superuser created successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to create Django superuser")
        # This is not a critical error, so continue


def main():
    """Main function."""
    print("Setting up the database...")
    
    # Ensure the database exists
    ensure_database_exists()
    
    # Run Prisma migrations
    run_prisma_migrate()
    
    # Run Django migrations
    run_django_migrations()
    
    # Create a superuser
    create_superuser()
    
    print("✅ Database setup completed successfully")


if __name__ == "__main__":
    main()
