<div align="center">

![Stars](https://img.shields.io/github/stars/Westhdon/OSINT-Manager?style=flat-square)
![Forks](https://img.shields.io/github/forks/Westhdon/OSINT-Manager?style=flat-square)
![Issues](https://img.shields.io/github/issues/Westhdon/OSINT-Manager?style=flat-square)
![License](https://img.shields.io/github/license/Westhdon/OSINT-Manager?style=flat-square)

[Follow Me →](https://github.com/Westhdon)

</div>

<div align="center">
## 🔍 OSINT-Manager
</div>

# About

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

Trying to implement frequent updates!

This project is a starting point for a more comprehensive OSINT CLI toolkit. Contributions and improvements are welcome!

This project is under the MIT license.

Note this project is mostly "vibe-coded".

This project is for EDUCATIONAL PURPOSES ONLY!
