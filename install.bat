@echo off
REM Installation/update script for Windows - installs or upgrades Python dependencies for OSINT Manager
echo Installing/updating dependencies from requirements.txt...
python -m pip install --user --upgrade -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)
echo Installation complete.
echo If the `holehe` command is not found, add your Python Scripts directory to PATH:
echo %%USERPROFILE%%\AppData\Roaming\Python\Python%%PYTHONVERSION%%\Scripts
echo (replace %%PYTHONVERSION%% with your Python version, e.g. 3.13)

REM automatically launch the main program after installing/updating
echo Launching OSINT Manager...
python main.py
