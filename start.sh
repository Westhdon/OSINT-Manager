#!/bin/bash
# Installation/update script for Unix-like systems
# Now includes many new features: Advanced search tools, batch operations, report generation, and more!
echo "Installing/updating dependencies from requirements.txt..."
echo "This may take a few minutes as new packages are installed..."
python3 -m pip install --user --upgrade -r requirements.txt
echo "Installation complete."
echo "All dependencies are ready, including new advanced features!"
echo "Ensure your user-level bin directory (e.g. ~/.local/bin) is in your PATH so that commands like 'holehe' work."
echo ""
echo "Launching OSINT Manager with all new features..."
echo "Features now include: Reverse IP lookup, SSL certificates, email verification,"
echo "username checker, batch operations, reports, CSV export, and more!"
echo ""
python3 main.py
