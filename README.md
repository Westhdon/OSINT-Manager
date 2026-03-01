# OSINT Manager

A command-line program to manage OSINT data and perform searches using several popular tools.

## Features

- Create and manage simple JSON-backed databases of email records
- **Holehe email enumeration** fully integrated (requires `holehe` package)
- **HaveIBeenPwned** breach lookup
- **WHOIS** domain lookup
- Optionally save scan results into a selected database
- DNS lookup (A, MX, NS records; install `dnspython` for full functionality)
- IP geolocation via the free ip-api.com service
- Configuration menu for storing API keys (HIBP, Shodan, etc.)

## Installation

Dependencies are listed in `requirements.txt`. To install them, run the appropriate script for your OS:

```bash
# Windows (PowerShell or CMD)
install.bat

# Unix / macOS
chmod +x install.sh
./install.sh
```

The scripts install packages using `pip --user`. You may need to add the Python `Scripts` folder (Windows) or `~/.local/bin` (Linux/macOS) to your `PATH` so that commands like `holehe` work globally.

## Usage

Run the main program using:

```bash
python main.py
```

Navigate the menus to manage databases or perform OSINT queries. When performing Holehe scans, you can choose to save positive results to a database for later review.

For Have I Been Pwned lookups you can set the `HIBP_API_KEY` environment variable to avoid rate limits.

## Extending the Tool

Additional OSINT integrations can be added by implementing new methods in `OSINTManager` and updating the menu structure. The modular design makes it easy to plug in new lookup functions.

---

This project is a starting point for a more comprehensive OSINT CLI toolkit. Contributions and improvements are welcome!
