# OSINT Manager

A command-line program to manage OSINT data and perform searches using several popular tools.

![Preview](preview.png)

## Features

- **Database Management** - Create, manage, and persist OSINT research data in JSON databases
- **Holehe email enumeration** fully integrated (requires `holehe` package) - Search email across 100+ platforms
- **HaveIBeenPwned** breach lookup - Check if email appears in known data breaches
- **WHOIS** domain lookup - Get registrant and technical information
- **DNS lookup** (A, MX, NS records; install `dnspython` for full functionality)
- **IP geolocation** via the free ip-api.com service
- **Reverse IP Lookup** - Find domains/services hosted on a specific IP address
- **Reverse DNS Lookup** - Get hostname from IP address
- **SSL Certificate Lookup** - Extract SSL certificate information from domains
- **Email Verification** - Check email format and MX records for deliverability
- **Username Availability Checker** - Check if a username exists on 15+ major platforms (Twitter, Instagram, GitHub, etc.)
- **Email Finder by Domain** - Find email addresses associated with company domains
- **Social Media Lookback** - Access whopostedwhat.com for historical social media posts
- **Subdomain Enumeration** - Find hidden subdomains using Certificate Transparency logs and DNS brute force
- **Person Search & OSINT** - Multiple methods to research people:
  - Search by name across social platforms
  - Search by username with automatic profile verification
  - Search by phone number (with links to lookup services)
  - Search by email to find associated social profiles
  - Reverse phone lookup tools
- **Advanced Search Tools** - Specialized lookup and intelligence gathering tools
- **Batch Operations** - Process multiple items at once:
  - Batch Email Breach Lookup - Check multiple emails simultaneously
  - Report Generation - Create comprehensive OSINT reports from database
  - CSV/JSON Export - Export all records for external analysis
- **Configuration menu** for storing API keys (HIBP, Shodan, etc.)
- **Save results** to selected databases for future reference and analysis

## Installation

[Instalation video for Windows.](https://www.youtube.com/watch?v=omylfrbhW-M)

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
10. **Advanced Search Tools** - Reverse IP/DNS lookup, SSL certificates, email verification, username availability
11. **Batch Operations** - Bulk email checks, report generation, CSV export
12. **Configuration** - Set up API keys for enhanced functionality
13. **Exit** - Close the application

Navigate the menus to manage databases or perform OSINT queries. When performing scans, you can save positive results to a database for later review.

## API Keys and Configuration

For Have I Been Pwned lookups you can set the `HIBP_API_KEY` environment variable to avoid rate limits. You can also manage API keys through the Configuration menu within the application for Shodan and other services.

## Extending the Tool

Additional OSINT integrations can be added by implementing new methods in `OSINTManager` and updating the menu structure. The modular design makes it easy to plug in new lookup functions.

## New Advanced Features (Latest Update)

### Advanced Search Tools
- **Reverse IP Lookup** - Find domains and services hosted on a specific IP address
- **SSL Certificate Extraction** - Get detailed SSL certificate information from domains including issuer, expiration, and alternative names
- **Email Address Verification** - Check email format validity and MX record existence for deliverability verification
- **Username Availability Checker** - Check if a username is claimed across 16+ major platforms with quick profile linking
- **Email Finder by Domain** - Discover email addresses associated with company domains using multiple services
- **Reverse DNS Lookup** - Convert IP addresses back to their associated hostnames

### Batch Operations & Reporting
- **Batch Email Breach Lookup** - Check multiple email addresses simultaneously against breach databases (respects rate limits)
- **OSINT Report Generation** - Create comprehensive text reports from your research database with statistics and formatting
- **CSV/JSON Export** - Export all database records to CSV format for use in external tools and analysis
- **Advanced Data Analysis** - Built-in summary statistics and cross-reference capabilities

### Enhanced Email Tools
- Full integration with Holehe for 100+ platform checking
- HaveIBeenPwned breach database integration
- Email format validation and MX record checking
- Batch processing capabilities

### Person & Username Research
- Name search across multiple social platforms with direct links
- Username verification across 16+ platforms (Twitter, Instagram, GitHub, Reddit, YouTube, TikTok, Twitch, and more)
- Automatic profile existence verification
- Phone number lookup tools and reverse phone lookup services
- Email-based social profile discovery

### Network & Domain Intelligence
- Complete WHOIS information retrieval
- Full DNS record lookups (A, MX, NS, SOA records)
- Subdomain enumeration using Certificate Transparency logs
- DNS brute force for common subdomains
- Reverse IP and Reverse DNS lookups
- SSL certificate analysis and vulnerability checking

## Disclaimer

**EDUCATIONAL PURPOSES ONLY**: This tool is designed for educational and authorized security research purposes only. Users are responsible for ensuring they have proper authorization before conducting any OSINT searches or investigations. The author assumes no liability for misuse, unauthorized access, or any damage resulting from the use of this tool.

**VIBE-CODED & SUPER-POWERED**: This project is "vibe-coded" - it's written with a casual, flexible approach to maximizing functionality and coolness! It now includes advanced features like reverse IP lookup, SSL certificate inspection, batch operations, report generation, and much more. Use at your own discretion.

---

This project is a starting point for a more comprehensive OSINT CLI toolkit. Contributions and improvements are welcome!

# About

A command-line program to manage OSINT data and perform searches using several popular tools.

## Features

- **Database Management** - Create, manage, and persist OSINT research data in JSON databases
- **Holehe email enumeration** fully integrated (requires `holehe` package) - Search email across 100+ platforms
- **HaveIBeenPwned** breach lookup - Check if email appears in known data breaches
- **WHOIS** domain lookup - Get registrant and technical information
- **DNS lookup** (A, MX, NS records; install `dnspython` for full functionality)
- **IP geolocation** via the free ip-api.com service
- **Reverse IP Lookup** - Find domains/services hosted on a specific IP address
- **Reverse DNS Lookup** - Get hostname from IP address
- **SSL Certificate Lookup** - Extract SSL certificate information from domains
- **Email Verification** - Check email format and MX records for deliverability
- **Username Availability Checker** - Check if a username exists on 15+ major platforms (Twitter, Instagram, GitHub, etc.)
- **Email Finder by Domain** - Find email addresses associated with company domains
- **Social Media Lookback** - Access whopostedwhat.com for historical social media posts
- **Subdomain Enumeration** - Find hidden subdomains using Certificate Transparency logs and DNS brute force
- **Person Search & OSINT** - Multiple methods to research people:
  - Search by name across social platforms
  - Search by username with automatic profile verification
  - Search by phone number (with links to lookup services)
  - Search by email to find associated social profiles
  - Reverse phone lookup tools
- **Advanced Search Tools** - Specialized lookup and intelligence gathering tools
- **Batch Operations** - Process multiple items at once:
  - Batch Email Breach Lookup - Check multiple emails simultaneously
  - Report Generation - Create comprehensive OSINT reports from database
  - CSV/JSON Export - Export all records for external analysis
- **Configuration menu** for storing API keys (HIBP, Shodan, etc.)
- **Save results** to selected databases for future reference and analysis

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

Run either start.sh, start.bat or start.exe.

or

```bash
python main.py
```
Note: this method avoides auto-updates and is not recommended.

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
10. **Advanced Search Tools** - Reverse IP/DNS lookup, SSL certificates, email verification, username availability
11. **Batch Operations** - Bulk email checks, report generation, CSV export
12. **Configuration** - Set up API keys for enhanced functionality
13. **Exit** - Close the application

Navigate the menus to manage databases or perform OSINT queries. When performing scans, you can save positive results to a database for later review.

## API Keys and Configuration

For Have I Been Pwned lookups you can set the `HIBP_API_KEY` environment variable to avoid rate limits. You can also manage API keys through the Configuration menu within the application for Shodan and other services.

## Extending the Tool

Additional OSINT integrations can be added by implementing new methods in `OSINTManager` and updating the menu structure. The modular design makes it easy to plug in new lookup functions.

## New Advanced Features (Latest Update)

### Advanced Search Tools
- **Reverse IP Lookup** - Find domains and services hosted on a specific IP address
- **SSL Certificate Extraction** - Get detailed SSL certificate information from domains including issuer, expiration, and alternative names
- **Email Address Verification** - Check email format validity and MX record existence for deliverability verification
- **Username Availability Checker** - Check if a username is claimed across 16+ major platforms with quick profile linking
- **Email Finder by Domain** - Discover email addresses associated with company domains using multiple services
- **Reverse DNS Lookup** - Convert IP addresses back to their associated hostnames

### Batch Operations & Reporting
- **Batch Email Breach Lookup** - Check multiple email addresses simultaneously against breach databases (respects rate limits)
- **OSINT Report Generation** - Create comprehensive text reports from your research database with statistics and formatting
- **CSV/JSON Export** - Export all database records to CSV format for use in external tools and analysis
- **Advanced Data Analysis** - Built-in summary statistics and cross-reference capabilities

### Enhanced Email Tools
- Full integration with Holehe for 100+ platform checking
- HaveIBeenPwned breach database integration
- Email format validation and MX record checking
- Batch processing capabilities

### Person & Username Research
- Name search across multiple social platforms with direct links
- Username verification across 16+ platforms (Twitter, Instagram, GitHub, Reddit, YouTube, TikTok, Twitch, and more)
- Automatic profile existence verification
- Phone number lookup tools and reverse phone lookup services
- Email-based social profile discovery

### Network & Domain Intelligence
- Complete WHOIS information retrieval
- Full DNS record lookups (A, MX, NS, SOA records)
- Subdomain enumeration using Certificate Transparency logs
- DNS brute force for common subdomains
- Reverse IP and Reverse DNS lookups
- SSL certificate analysis and vulnerability checking

## Disclaimer

**EDUCATIONAL PURPOSES ONLY**: This tool is designed for educational and authorized security research purposes only. Users are responsible for ensuring they have proper authorization before conducting any OSINT searches or investigations. The author assumes no liability for misuse, unauthorized access, or any damage resulting from the use of this tool.

**VIBE-CODED & SUPER-POWERED**: This project is "vibe-coded" - it's written with a casual, flexible approach to maximizing functionality and coolness! It now includes advanced features like reverse IP lookup, SSL certificate inspection, batch operations, report generation, and much more. Use at your own discretion.

---

This project is a starting point for a more comprehensive OSINT CLI toolkit. Contributions and improvements are welcome!
