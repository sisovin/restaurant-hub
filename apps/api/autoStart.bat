@echo off
echo Restaurant Hub API Auto Start Script
echo ===================================

REM Step 1: Create Python virtual environment if it doesn't exist
if not exist venv (
    echo Creating Python virtual environment...
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Step 2: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Step 3: Install dependencies if needed
if exist requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Step 4: Run the development server
echo Starting development server...
python manage.py runserver

REM Keep the window open if there's an error
if %ERRORLEVEL% neq 0 (
    echo An error occurred while starting the server.
    pause
)