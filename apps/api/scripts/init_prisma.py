"""
Script to initialize Prisma and generate the Prisma client.
"""

import os
import subprocess
import sys
from pathlib import Path


def ensure_prisma_installed():
    """Ensure prisma is installed."""
    try:
        # Check if prisma CLI is available
        subprocess.run(['prisma', '--version'], check=True, capture_output=True)
        print("✅ Prisma CLI is already installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Prisma CLI not found. Installing...")
        try:
            # Install prisma globally using npm
            subprocess.run(['npm', 'install', '-g', 'prisma'], check=True)
            print("✅ Prisma CLI installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install Prisma CLI. Please install it manually using 'npm install -g prisma'")
            sys.exit(1)


def ensure_prisma_client_py_installed():
    """Ensure prisma-client-py is installed."""
    try:
        # Check if prisma-client-py is installed
        import prisma  # noqa
        print("✅ prisma-client-py is already installed")
    except ImportError:
        print("❌ prisma-client-py not found. Installing...")
        try:
            # Install prisma-client-py using pip
            subprocess.run(['pip', 'install', 'prisma'], check=True)
            print("✅ prisma-client-py installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install prisma-client-py. Please install it manually using 'pip install prisma'")
            sys.exit(1)


def generate_prisma_client():
    """Generate Prisma client from schema."""
    print("Generating Prisma client...")
    
    # Get the path to the Prisma schema
    base_dir = Path(__file__).resolve().parent.parent
    schema_path = os.path.join(base_dir, 'prisma', 'schema.prisma')
    
    # Check if the schema file exists
    if not os.path.exists(schema_path):
        print(f"❌ Schema file not found at {schema_path}")
        sys.exit(1)
    
    try:
        # Generate the Prisma client
        subprocess.run(['prisma', 'generate', '--schema', schema_path], check=True)
        print("✅ Prisma client generated successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to generate Prisma client")
        sys.exit(1)


def main():
    """Main function."""
    print("Initializing Prisma...")
    
    # Ensure required tools are installed
    ensure_prisma_installed()
    ensure_prisma_client_py_installed()
    
    # Generate Prisma client
    generate_prisma_client()
    
    print("✅ Prisma initialization completed successfully")


if __name__ == "__main__":
    main()
