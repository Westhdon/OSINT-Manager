<div align="center">

![Stars](https://img.shields.io/github/stars/Westhdon/OSINT-Manager?style=flat-square)
![Forks](https://img.shields.io/github/forks/Westhdon/OSINT-Manager?style=flat-square)
![Issues](https://img.shields.io/github/issues/Westhdon/OSINT-Manager?style=flat-square)
![License](https://img.shields.io/github/license/Westhdon/OSINT-Manager?style=flat-square)

[Follow Me →](https://github.com/Westhdon)

</div>

<div align="center">
🔍 OSINT-Manager
</div>

# About

A command-line program to manage OSINT data and perform searches using several popular tools.

## Features

- Create and manage simple JSON-backed databases of records
- **Holehe email enumeration** fully integrated (requires `holehe` package)
- **HaveIBeenPwned** breach lookup
- **WHOIS** domain lookup
- **DNS lookup** (A, MX, NS records; install `dnspython` for full functionality)
- **IP geolocation** via the free ip-api.com service
- **Social Media Lookback** - Open whopostedwhat.com to search historical social media posts
- **Subdomain Enumeration** - Find hidden subdomains using Certificate Transparency logs and DNS brute force
- **Person Search & OSINT** - Multiple methods to research people:
  - Search by name across social platforms
  - Search by username with automatic profile verification
  - Search by phone number (with links to lookup services)
  - Search by email to find associated social profiles
  - Reverse phone lookup tools
- **Configuration menu** for storing API keys (HIBP, Shodan, etc.)
- Save all scan results into selected databases for future reference

## Installation

Dependencies are listed in `requirements.txt`. To install or update them, simply run the appropriate script for your OS. The install scripts now perform an upgrade of any existing packages and **automatically launch the program** once the dependencies are ready.

```bash
# Windows (PowerShell or CMD)
install.bat

# Unix / macOS
chmod +x install.sh
./install.sh
```

Running the script will install or upgrade all packages in the requirements file and then start `main.py`. You can re‑run the installer at any time to update to newer dependency versions.

The scripts install packages using `pip --user`. You may need to add the Python `Scripts` folder (Windows) or `~/.local/bin` (Linux/macOS) to your `PATH` so that commands like `holehe` work globally.

Configuration is persisted in `config.json` (created automatically). You can manage API keys through the configuration menu in the application or by editing this file directly.

## Usage

Run the main program using:

```bash
python main.py
```

### Main Menu Options

1. **Database Management** - Create, delete, and manage JSON databases
2. **Email Search (Holehe)** - Search email addresses across 100+ platforms
3. **Email Search (HaveIBeenPwned)** - Check if emails appear in known breaches
4. **Domain Lookup (WHOIS)** - Get WHOIS information for domains
5. **DNS Lookup** - Query A, MX, and NS records
6. **IP Geolocation** - Find the geographic location of IP addresses
7. **Social Media Lookback** - Access whopostedwhat.com for historical social media data
8. **Subdomain Enumeration** - Discover hidden subdomains and enumerate potential attack surfaces
9. **Person Search & OSINT** - Research individuals through multiple methods
10. **Configuration** - Set up API keys for enhanced functionality
11. **Exit** - Close the application

Navigate the menus to manage databases or perform OSINT queries. When performing scans, you can save positive results to a database for later review.

## API Keys and Configuration

For Have I Been Pwned lookups you can set the `HIBP_API_KEY` environment variable to avoid rate limits. You can also manage API keys through the Configuration menu within the application for Shodan and other services.

## Extending the Tool

Additional OSINT integrations can be added by implementing new methods in `OSINTManager` and updating the menu structure. The modular design makes it easy to plug in new lookup functions.

## Disclaimer

**EDUCATIONAL PURPOSES ONLY**: This tool is designed for educational and authorized security research purposes only. Users are responsible for ensuring they have proper authorization before conducting any OSINT searches or investigations. The author assumes no liability for misuse, unauthorized access, or any damage resulting from the use of this tool.

**VIBE-CODED**: This project is "vibe-coded" - it's written with a casual, flexible approach to functionality and may not follow strict production standards. Use at your own discretion.

---

This project is a starting point for a more comprehensive OSINT CLI toolkit. Contributions and improvements are welcome!
**

# Latest update:
02-03-2026 14:45
