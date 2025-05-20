@echo off
echo Restaurant Hub API Setup Script
echo ==============================

echo Installing Python dependencies...
pip install -r requirements.txt

echo Installing Prisma CLI...
npm install -g prisma

echo Initializing Prisma...
python scripts/init_prisma.py

echo Setting up the database...
python scripts/setup_db.py

echo Loading test data...
python scripts/init_test_data.py

echo Setup complete! You can now run the development server with:
echo python manage.py runserver
