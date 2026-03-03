@echo off
REM Installation/update script for Windows - installs or upgrades Python dependencies for OSINT Manager
REM This script now includes many new features: Advanced search tools, batch operations, report generation, and more!
echo Installing/updating dependencies from requirements.txt...
echo This may take a few minutes as new packages are installed...
python -m pip install --user --upgrade -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)
echo Installation complete.
echo All dependencies are ready, including new advanced features!
echo If the `holehe` command is not found, add your Python Scripts directory to PATH:
echo %%USERPROFILE%%\AppData\Roaming\Python\Python%%PYTHONVERSION%%\Scripts
echo (replace %%PYTHONVERSION%% with your Python version, e.g. 3.13)

REM automatically launch the main program after installing/updating
echo.
echo Launching OSINT Manager with all new features...
echo Features now include: Reverse IP lookup, SSL certificates, email verification, 
echo username checker, batch operations, reports, CSV export, and more!
echo.
python main.py
