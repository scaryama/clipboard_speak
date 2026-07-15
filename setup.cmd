@echo off
echo ========================================
echo    clipboard_speak Setup
echo ========================================

:: Create virtual environment if it doesn't exist
if not exist .venv (
    echo [1/3] Creating virtual environment...
    py -m venv .venv
) else (
    echo [1/3] Virtual environment already exists.
)

:: Activate virtual environment
echo [2/3] Activating virtual environment...
call .venv\Scripts\activate.bat

:: Upgrade pip and install requirements
echo [3/3] Upgrading pip and installing packages...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo    ✅ Setup Complete!
echo.
echo    How to use:
echo    1. .venv\Scripts\activate.bat     (Activate)
echo    2. python main.py                 (Run the program)
echo ========================================
pause