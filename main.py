#!/usr/bin/env python3
"""
OSINT Manager - A professional CLI tool for OSINT data management
Manage databases and search email information across platforms

Features:
- Database creation, record management, and search
- Integrated Holehe email enumeration (full programmatic access)
- HaveIBeenPwned breach lookup
- WHOIS domain lookup

Run `install.bat` (Windows) or `install.sh` (Unix) to install or update required packages. The installer scripts now upgrade any existing dependencies and automatically launch the program when they finish.
"""

import os
import sys
import json

import webbrowser
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

# Color codes for professional CLI output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class OSINTManager:
    def __init__(self):
        self.db_dir = Path("databases")
        self.db_dir.mkdir(exist_ok=True)
        self.current_db = None
        self.config_file = Path("config.json")
        self.config: Dict = {}
        self.load_config()

    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    # --------------------------------------------------
    # Configuration helpers
    # --------------------------------------------------
    def load_config(self):
        """Load configuration (API keys etc.) from disk."""
        if self.config_file.exists():
            try:
                self.config = json.loads(self.config_file.read_text())
            except Exception:
                self.config = {}
        else:
            self.config = {}

    def save_config(self):
        """Persist current configuration to disk."""
        try:
            self.config_file.write_text(json.dumps(self.config, indent=2))
        except Exception as e:
            self.print_error(f"Failed to save config: {e}")

    def print_header(self, title: str):
        """Print formatted header"""
        self.clear_screen()
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.CYAN}  {title.center(56)}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}\n")

    def print_menu(self, options: List[str]):
        """Print formatted menu options"""
        for i, option in enumerate(options, 1):
            print(f"  {Colors.BLUE}[{i}]{Colors.ENDC} {option}")
        print()

    def print_success(self, message: str):
        """Print success message"""
        # use ASCII checkmark to avoid encoding issues
        print(f"{Colors.GREEN}[OK] {message}{Colors.ENDC}\n")

    def print_error(self, message: str):
        """Print error message"""
        print(f"{Colors.RED}[ERROR] {message}{Colors.ENDC}\n")

    def print_info(self, message: str):
        """Print info message"""
        # use simple 'i' for information
        print(f"{Colors.YELLOW}[i] {message}{Colors.ENDC}\n")

    def input_prompt(self, prompt: str = "Enter option") -> str:
        """Print formatted input prompt"""
        # use ASCII arrow to maintain compatibility with Windows consoles
        return input(f"{Colors.BLUE}->{Colors.ENDC} {prompt}: ").strip()

    def list_databases(self) -> List[str]:
        """List all available databases"""
        db_files = [f.stem for f in self.db_dir.glob("*.txt")]
        return sorted(db_files)

    def create_database(self):
        """Create a new database"""
        self.print_header("CREATE DATABASE")
        db_name = self.input_prompt("Enter database name").strip()
        
        if not db_name:
            self.print_error("Database name cannot be empty")
            return
        
        db_path = self.db_dir / f"{db_name}.txt"
        
        if db_path.exists():
            self.print_error(f"Database '{db_name}' already exists")
            return
        
        db_path.write_text(json.dumps({"created": datetime.now().isoformat(), "records": []}, indent=2))
        self.print_success(f"Database '{db_name}' created successfully")
        input("Press Enter to continue...")

    def delete_database(self):
        """Delete an existing database"""
        self.print_header("DELETE DATABASE")
        databases = self.list_databases()
        
        if not databases:
            self.print_info("No databases found")
            input("Press Enter to continue...")
            return
        
        self.print_info("Available databases:")
        self.print_menu(databases + ["Cancel"])
        
        choice = self.input_prompt("Select database to delete")
        
        try:
            idx = int(choice) - 1
            if idx == len(databases):
                return
            if 0 <= idx < len(databases):
                confirm = self.input_prompt(f"Delete '{databases[idx]}'? (yes/no)").lower()
                if confirm == "yes":
                    (self.db_dir / f"{databases[idx]}.txt").unlink()
                    self.print_success(f"Database '{databases[idx]}' deleted")
        except (ValueError, IndexError):
            self.print_error("Invalid selection")
        
        input("Press Enter to continue...")

    def manage_database(self):
        """Manage database records"""
        self.print_header("MANAGE DATABASE")
        databases = self.list_databases()
        
        if not databases:
            self.print_info("No databases found")
            input("Press Enter to continue...")
            return
        
        self.print_info("Available databases:")
        self.print_menu(databases + ["Back"])
        
        choice = self.input_prompt("Select database")
        
        try:
            idx = int(choice) - 1
            if idx == len(databases):
                return
            if 0 <= idx < len(databases):
                self.current_db = databases[idx]
                self.manage_db_menu()
        except ValueError:
            self.print_error("Invalid selection")
            input("Press Enter to continue...")

    def manage_db_menu(self):
        """Submenu for managing database records"""
        while True:
            self.print_header(f"MANAGE DATABASE: {self.current_db}")
            self.print_menu([
                "View records",
                "Add record",
                "Search record",
                "Delete record",
                "Back to Database Menu"
            ])
            
            choice = self.input_prompt("Select option")
            
            if choice == "1":
                self.view_records()
            elif choice == "2":
                self.add_record()
            elif choice == "3":
                self.search_record()
            elif choice == "4":
                self.delete_record()
            elif choice == "5":
                break
            else:
                self.print_error("Invalid option")
                input("Press Enter to continue...")

    def view_records(self):
        """View all records in current database"""
        self.print_header("VIEW RECORDS")
        db_path = self.db_dir / f"{self.current_db}.txt"
        
        try:
            data = json.loads(db_path.read_text())
            records = data.get("records", [])
            
            if not records:
                self.print_info("No records in this database")
            else:
                print(f"{Colors.BOLD}Total records: {len(records)}{Colors.ENDC}\n")
                for i, record in enumerate(records, 1):
                    print(f"{Colors.CYAN}Record #{i}{Colors.ENDC}")
                    for key, value in record.items():
                        print(f"  {key}: {value}")
                    print()
        except Exception as e:
            self.print_error(f"Error reading records: {str(e)}")
        
        input("Press Enter to continue...")

    def add_record(self):
        """Add new record to database"""
        self.print_header("ADD RECORD")
        email = self.input_prompt("Enter email")
        platform = self.input_prompt("Enter platform (optional, or press Enter for manual entry)")
        data_found = self.input_prompt("Data found? (yes/no)")
        notes = self.input_prompt("Notes (optional)")
        
        db_path = self.db_dir / f"{self.current_db}.txt"
        
        try:
            data = json.loads(db_path.read_text())
            record = {
                "email": email,
                "platform": platform or "Custom",
                "data_found": data_found,
                "notes": notes,
                "timestamp": datetime.now().isoformat()
            }
            data["records"].append(record)
            db_path.write_text(json.dumps(data, indent=2))
            self.print_success("Record added successfully")
        except Exception as e:
            self.print_error(f"Error adding record: {str(e)}")
        
        input("Press Enter to continue...")

    def search_record(self):
        """Search for records"""
        self.print_header("SEARCH RECORD")
        query = self.input_prompt("Enter email to search").lower()
        db_path = self.db_dir / f"{self.current_db}.txt"
        
        try:
            data = json.loads(db_path.read_text())
            results = [r for r in data.get("records", []) if query in r.get("email", "").lower()]
            
            if results:
                print(f"{Colors.GREEN}Found {len(results)}{Colors.ENDC}\n")
                for record in results:
                    for key, value in record.items():
                        print(f"  {key}: {value}")
                    print()
            else:
                self.print_info("No records found")
        except Exception as e:
            self.print_error(f"Error searching records: {str(e)}")
        
        input("Press Enter to continue...")

    def delete_record(self):
        """Delete a record from database"""
        self.print_header("DELETE RECORD")
        email = self.input_prompt("Enter email of record to delete")
        db_path = self.db_dir / f"{self.current_db}.txt"
        
        try:
            data = json.loads(db_path.read_text())
            original_count = len(data["records"])
            data["records"] = [r for r in data["records"] if r.get("email") != email]
            
            if len(data["records"]) < original_count:
                db_path.write_text(json.dumps(data, indent=2))
                self.print_success("Record deleted successfully")
            else:
                self.print_info("No matching record found")
        except Exception as e:
            self.print_error(f"Error deleting record: {str(e)}")
        
        input("Press Enter to continue...")

    # -------------------------------------
    # Holehe integration helpers
    # -------------------------------------
    def _search_email_holehe(self, email: str, platform: Optional[str] = None) -> Optional[List[Dict]]:
        """Internal helper: use holehe modules to query an email.

        Returns a list of result dicts or None if an error occurred.
        """
        try:
            import holehe.core as hhcore
            import trio
            import httpx
        except ImportError:
            self.print_error("The 'holehe' package is not installed. Please run the install script or `pip install holehe`.")
            return None

        # load all supported site modules
        modules = hhcore.import_submodules("holehe.modules")
        websites = hhcore.get_functions(modules)

        # filter by platform name if requested
        if platform:
            websites = [w for w in websites if w.__name__.lower() == platform.lower()]
            if not websites:
                return []

        # asynchronous runner
        async def run_all():
            client = httpx.AsyncClient(timeout=10)
            out = []
            # add progress bar if available
            try:
                from holehe.instruments import TrioProgress
                instr = TrioProgress(len(websites))
                trio.lowlevel.add_instrument(instr)
            except Exception:
                instr = None

            async with trio.open_nursery() as nursery:
                for site in websites:
                    nursery.start_soon(hhcore.launch_module, site, email, client, out)
            if instr:
                trio.lowlevel.remove_instrument(instr)
            await client.aclose()
            return sorted(out, key=lambda i: i.get("name"))

        try:
            return trio.run(run_all)
        except Exception as e:
            self.print_error(f"Holehe execution error: {e}")
            return None

    def search_email_holehe(self):
        """Search email using Holehe (full integration)."""
        self.print_header("EMAIL SEARCH - HOLEHE")
        self.print_info("Requires the 'holehe' Python package. Run the install script if you haven't installed dependencies.")

        self.print_menu([
            "Check specific platform",
            "Check all platforms",
            "Back to Main Menu"
        ])

        choice = self.input_prompt("Select option")

        if choice == "1":
            self.check_specific_platform()
        elif choice == "2":
            self.check_all_platforms()
        elif choice != "3":
            self.print_error("Invalid option")
            input("Press Enter to continue...")

    def check_specific_platform(self):
        """Check email on a single platform using holehe modules."""
        self.print_header("CHECK SPECIFIC PLATFORM")
        email = self.input_prompt("Enter email to check")
        platform = self.input_prompt("Enter platform name").lower()
        
        try:
            results = self._search_email_holehe(email, platform)
            if results is None:
                # error already shown
                pass
            elif not results:
                self.print_info(f"No results for platform '{platform}' or platform not found in holehe modules.")
            else:
                self.print_success(f"Results for {email} on {platform}:")
                for r in results:
                    for k, v in r.items():
                        print(f"  {k}: {v}")
                    print()
                # offer to save positive result
                if any(r.get('exists') for r in results):
                    save = self.input_prompt("Save positive result to a database? (yes/no)").lower()
                    if save == 'yes' and self.ensure_database_selected():
                        for r in results:
                            if r.get('exists'):
                                self.add_record_programmatic(email, r.get('domain'), 'yes', notes="holehe scan")
                        self.print_success("Results stored in database")
        except Exception as e:
            self.print_error(f"Error: {str(e)}")
        
        input("Press Enter to continue...")

    def check_all_platforms(self):
        """Run holehe scan across all supported platforms for an email."""
        self.print_header("CHECK ALL PLATFORMS")
        email = self.input_prompt("Enter email to check")
        
        try:
            results = self._search_email_holehe(email)
            if results is None:
                pass
            elif not results:
                self.print_info("No results returned")
            else:
                self.print_success(f"Found {len(results)} entries")
                for r in results:
                    line = f"{r.get('domain')} : "
                    if r.get('exists'):
                        line += Colors.GREEN + "FOUND" + Colors.ENDC
                    elif r.get('rateLimit'):
                        line += Colors.RED + "RATE-LIMIT" + Colors.ENDC
                    else:
                        line += Colors.RED + "NOT FOUND" + Colors.ENDC
                    print(line)
                print()
                if any(r.get('exists') for r in results):
                    save = self.input_prompt("Save all positive results to a database? (yes/no)").lower()
                    if save == 'yes' and self.ensure_database_selected():
                        for r in results:
                            if r.get('exists'):
                                self.add_record_programmatic(email, r.get('domain'), 'yes', notes="holehe scan")
                        self.print_success("Results stored in database")
        except Exception as e:
            self.print_error(f"Error: {str(e)}")
        
        input("Press Enter to continue...")

    # ------------------------------------------------------------------
    # Additional OSINT tool wrappers
    # ------------------------------------------------------------------
    def search_email_hibp(self):
        """Check if an email appears in data breaches via Have I Been Pwned API."""
        self.print_header("EMAIL SEARCH - HAVE I BEEN PWNED")
        self.print_info("No API key required for limited usage; set HIBP_API_KEY env var for full access.")
        email = self.input_prompt("Enter email to search")
        try:
            import requests
            headers = {"User-Agent": "osint-manager"}
            api_key = os.environ.get("HIBP_API_KEY") or self.config.get("hibp_api_key")
            if api_key:
                headers["hibp-api-key"] = api_key
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            resp = requests.get(url, headers=headers, params={"truncateResponse": "false"})
            if resp.status_code == 200:
                breaches = resp.json()
                self.print_success(f"Found {len(breaches)} breach(es)")
                for b in breaches:
                    print(f" - {b.get('Name')} ({b.get('BreachDate')}) - {b.get('Title')}")
            elif resp.status_code == 404:
                self.print_info("No breaches found for that email")
            else:
                self.print_error(f"HIBP error {resp.status_code}: {resp.text}")
        except Exception as e:
            self.print_error(f"Error querying HIBP: {e}")
        input("Press Enter to continue...")

    def search_domain_whois(self):
        """Perform a WHOIS lookup on a domain."""
        self.print_header("DOMAIN LOOKUP - WHOIS")
        domain = self.input_prompt("Enter domain (e.g., example.com)")
        try:
            import whois
            w = whois.whois(domain)
            # whois returns a dict-like object
            for key, val in w.items():
                print(f"{key}: {val}")
        except Exception as e:
            self.print_error(f"WHOIS lookup failed: {e}")
        input("Press Enter to continue...")

    def ensure_database_selected(self) -> bool:
        """Ensure `self.current_db` points to an existing database.

        If none is selected the user is prompted to choose one. Returns True
        when a database is available for writing.
        """
        if self.current_db:
            return True
        databases = self.list_databases()
        if not databases:
            self.print_error("No databases exist. Create one first.")
            input("Press Enter to continue...")
            return False
        self.print_info("Select a database to use for storing results:")
        self.print_menu(databases + ["Cancel"])
        choice = self.input_prompt("Select database")
        try:
            idx = int(choice) - 1
            if idx == len(databases):
                return False
            if 0 <= idx < len(databases):
                self.current_db = databases[idx]
                return True
        except ValueError:
            pass
        self.print_error("Invalid selection")
        input("Press Enter to continue...")
        return False

    def add_record_programmatic(self, email: str, platform: str, data_found: str, notes: str = ""):
        """Add a record to the currently selected database without prompting."""
        if not self.current_db:
            return
        db_path = self.db_dir / f"{self.current_db}.txt"
        try:
            data = json.loads(db_path.read_text())
            record = {
                "email": email,
                "platform": platform,
                "data_found": data_found,
                "notes": notes,
                "timestamp": datetime.now().isoformat()
            }
            data["records"].append(record)
            db_path.write_text(json.dumps(data, indent=2))
        except Exception:
            pass

    def database_menu(self):
        """Database management menu"""
        while True:
            self.print_header("DATABASE MANAGEMENT")
            self.print_menu([
                "Create Database",
                "Delete Database",
                "Manage Database",
                "Back to Main Menu"
            ])

            choice = self.input_prompt("Select option")

            if choice == "1":
                self.create_database()
            elif choice == "2":
                self.delete_database()
            elif choice == "3":
                self.manage_database()
            elif choice == "4":
                break
            else:
                self.print_error("Invalid option")
                input("Press Enter to continue...")

    def main_menu(self):
        """Main application menu"""
        while True:
            self.print_header("OSINT MANAGER")
            self.print_menu([
                "Database Management",
                "Email Search (Holehe)",
                "Email Search (HaveIBeenPwned)",
                "Domain Lookup (WHOIS)",
                "Exit"
            ])

            choice = self.input_prompt("Select option")

            if choice == "1":
                self.database_menu()
            elif choice == "2":
                self.search_email_holehe()
            elif choice == "3":
                self.search_email_hibp()
            elif choice == "4":
                self.search_domain_whois()
            elif choice == "5":
                self.print_header("GOODBYE")
                print(f"{Colors.CYAN}Thank you for using OSINT Manager{Colors.ENDC}\n")
                sys.exit(0)
            else:
                self.print_error("Invalid option")
                input("Press Enter to continue...")

    def configure_api_keys(self):
        """Menu for entering/viewing API keys."""
        while True:
            self.print_header("CONFIGURATION - API KEYS")
            self.print_menu([
                "Set HaveIBeenPwned API Key",
                "Set Shodan API Key",
                "View current keys",
                "Back"
            ])
            choice = self.input_prompt("Select option")
            if choice == '1':
                key = self.input_prompt("Enter HIBP API key (leave blank to clear)")
                if key:
                    self.config['hibp_api_key'] = key
                    self.print_success("HIBP key saved")
                else:
                    self.config.pop('hibp_api_key', None)
                    self.print_info("HIBP key cleared")
                self.save_config()
                input("Press Enter to continue...")
            elif choice == '2':
                key = self.input_prompt("Enter Shodan API key (leave blank to clear)")
                if key:
                    self.config['shodan_api_key'] = key
                    self.print_success("Shodan key saved")
                else:
                    self.config.pop('shodan_api_key', None)
                    self.print_info("Shodan key cleared")
                self.save_config()
                input("Press Enter to continue...")
            elif choice == '3':
                self.print_header("CURRENT API KEYS")
                for name in ['hibp_api_key','shodan_api_key']:
                    val = self.config.get(name)
                    display = val[:4] + '...' if val else '<not set>'
                    print(f"{name}: {display}")
                input("Press Enter to continue...")
            elif choice == '4':
                break
            else:
                self.print_error("Invalid option")
                input("Press Enter to continue...")

    def lookup_dns_records(self):
        """Perform DNS lookups for a domain."""
        self.print_header("DNS LOOKUP")
        domain = self.input_prompt("Enter domain (e.g. example.com)")
        try:
            import socket
            self.print_info("A records:")
            a = socket.gethostbyname_ex(domain)
            # a = (hostname, aliaslist, ipaddrlist)
            for ip in a[2]:
                print(f" - {ip}")
        except Exception as e:
            self.print_error(f"A lookup failed: {e}")
        try:
            # attempt MX/NS via dnspython if available
            import dns.resolver
            self.print_info("MX records:")
            for r in dns.resolver.resolve(domain, 'MX'):
                print(f" - {r.exchange} priority {r.preference}")
            self.print_info("NS records:")
            for r in dns.resolver.resolve(domain, 'NS'):
                print(f" - {r.target}")
        except ImportError:
            self.print_info("Install 'dnspython' to see MX/NS records")
        except Exception as e:
            self.print_error(f"Additional DNS query failed: {e}")
        input("Press Enter to continue...")

    def social_media_lookback(self):
        """Open whopostedwhat.com for social media lookback."""
        self.print_header("SOCIAL MEDIA LOOKBACK")
        self.print_info("Opening https://whopostedwhat.com/ in your default browser...")
        try:
            webbrowser.open("https://whopostedwhat.com/")
            self.print_success("Browser opened successfully")
        except Exception as e:
            self.print_error(f"Failed to open browser: {e}")
        input("Press Enter to continue...")

    def ip_geolocation(self):
        """Look up geolocation for an IP address using free ip-api.com service."""
        self.print_header("IP GEOLOCATION")
        ip = self.input_prompt("Enter IP address or hostname")
        try:
            import requests
            resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            data = resp.json()
            if data.get('status') == 'success':
                for k in ['query','country','regionName','city','isp','org','as']:
                    print(f"{k}: {data.get(k)}")
            else:
                self.print_error(f"Lookup failed: {data.get('message')}")
        except Exception as e:
            self.print_error(f"Error performing geolocation: {e}")
        input("Press Enter to continue...")

    def find_subdomains(self):
        """Find subdomains using Certificate Transparency logs and DNS brute force."""
        self.print_header("SUBDOMAIN ENUMERATION")
        domain = self.input_prompt("Enter domain (e.g., example.com)")
        
        if not domain:
            self.print_error("Domain cannot be empty")
            input("Press Enter to continue...")
            return
        
        subdomains = set()
        
        # Method 1: Query crt.sh (Certificate Transparency logs)
        self.print_info("Searching Certificate Transparency logs via crt.sh...")
        try:
            import requests
            url = f"https://crt.sh/?q=%.{domain}&output=json"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                certs = resp.json()
                for cert in certs:
                    name = cert.get('name_value', '')
                    # Extract subdomains from name_value (can contain multiple domains)
                    names = name.split('\n')
                    for n in names:
                        n = n.strip()
                        if n and n.endswith(domain):
                            # Remove wildcard if present
                            n = n.replace('*.', '')
                            subdomains.add(n)
            self.print_success(f"Found {len(subdomains)} subdomains from crt.sh")
        except Exception as e:
            self.print_error(f"crt.sh search failed: {e}")
        
        # Method 2: Attempt common subdomain prefixes
        self.print_info("Attempting DNS resolution of common subdomains...")
        common_prefixes = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'ns2',
            'cpanel', 'whm', 'autodiscover', 'autoconfig', 'admin', 'test', 'dev', 'staging',
            'api', 'cdn', 'img', 'images', 'static', 'assets', 'files', 'downloads',
            'blog', 'shop', 'store', 'support', 'help', 'contact', 'mail1', 'server',
            'database', 'db', 'backup', 'old', 'temp', 'vpn', 'internal', 'secure'
        ]
        
        found_count = 0
        try:
            import socket
            for prefix in common_prefixes:
                subdomain = f"{prefix}.{domain}"
                try:
                    socket.gethostbyname(subdomain)
                    subdomains.add(subdomain)
                    found_count += 1
                except socket.gaierror:
                    pass
                except Exception:
                    pass
            self.print_success(f"Successfully resolved {found_count} common subdomains")
        except Exception as e:
            self.print_error(f"DNS brute force failed: {e}")
        
        # Display results
        if subdomains:
            self.print_success(f"Found {len(subdomains)} unique subdomains:")
            for subdomain in sorted(subdomains):
                print(f"  - {subdomain}")
            print()
            
            # Option to save to database
            save = self.input_prompt("Save results to database? (yes/no)").lower()
            if save == 'yes' and self.ensure_database_selected():
                try:
                    db_path = self.db_dir / f"{self.current_db}.txt"
                    data = json.loads(db_path.read_text())
                    for subdomain in subdomains:
                        record = {
                            "domain": domain,
                            "subdomain": subdomain,
                            "notes": "enumeration",
                            "timestamp": datetime.now().isoformat()
                        }
                        data["records"].append(record)
                    db_path.write_text(json.dumps(data, indent=2))
                    self.print_success(f"Saved {len(subdomains)} subdomains to database")
                except Exception as e:
                    self.print_error(f"Failed to save to database: {e}")
        else:
            self.print_info("No subdomains found")
        
        input("Press Enter to continue...")

    def person_search(self):
        """Search for information about a person using multiple methods."""
        self.print_header("PERSON SEARCH & OSINT")
        self.print_menu([
            "Search by Name",
            "Search by Username",
            "Search by Phone Number",
            "Search by Email (Social profiles)",
            "Reverse Phone Lookup",
            "Back to Main Menu"
        ])
        
        choice = self.input_prompt("Select search method")
        
        if choice == "1":
            self.search_person_by_name()
        elif choice == "2":
            self.search_person_by_username()
        elif choice == "3":
            self.search_person_by_phone()
        elif choice == "4":
            self.search_person_by_email()
        elif choice == "5":
            self.reverse_phone_lookup()
        elif choice != "6":
            self.print_error("Invalid option")
            input("Press Enter to continue...")

    def search_person_by_name(self):
        """Search for a person by name across public sources."""
        self.print_header("SEARCH BY NAME")
        first_name = self.input_prompt("Enter first name")
        last_name = self.input_prompt("Enter last name")
        
        if not first_name or not last_name:
            self.print_error("Name cannot be empty")
            input("Press Enter to continue...")
            return
        
        results = []
        full_name = f"{first_name} {last_name}"
        
        # Search across major social platforms and people search engines
        self.print_info("Searching across multiple sources...")
        
        social_platforms = [
            ("Facebook", f"https://facebook.com/search/people/?q={first_name}+{last_name}"),
            ("Twitter", f"https://twitter.com/search?q={first_name}%20{last_name}&type=users"),
            ("LinkedIn", f"https://www.linkedin.com/search/results/people/?keywords={first_name}%20{last_name}"),
            ("Instagram", f"https://www.instagram.com/explore/tags/{first_name}{last_name}/"),
            ("YouTube", f"https://www.youtube.com/results?search_query={first_name}+{last_name}"),
            ("GitHub", f"https://github.com/search?q={first_name}+{last_name}&type=users"),
            ("Reddit", f"https://www.reddit.com/search/?q={first_name}%20{last_name}"),
        ]
        
        self.print_success(f"Search URLs for '{full_name}':")
        for platform, url in social_platforms:
            print(f"  {Colors.CYAN}{platform}{Colors.ENDC}: {url}")
            results.append({"platform": platform, "url": url})
        
        print()
        
        # Try to fetch from Google Custom Search or similar
        try:
            import requests
            # Using DuckDuckGo which doesn't require API key (basic search)
            search_query = f"{first_name}+{last_name}"
            url = f"https://duckduckgo.com/search?q={search_query}&format=json"
            resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            if resp.status_code == 200:
                self.print_info("DuckDuckGo search query:")
                print(f"  https://duckduckgo.com/?q={search_query.replace('+', '%20')}")
        except Exception as e:
            pass
        
        # Option to save results
        save = self.input_prompt("Save search results to database? (yes/no)").lower()
        if save == 'yes' and self.ensure_database_selected():
            try:
                db_path = self.db_dir / f"{self.current_db}.txt"
                data = json.loads(db_path.read_text())
                record = {
                    "name": full_name,
                    "search_type": "person_by_name",
                    "platforms": [r["platform"] for r in results],
                    "timestamp": datetime.now().isoformat()
                }
                data["records"].append(record)
                db_path.write_text(json.dumps(data, indent=2))
                self.print_success("Search results saved to database")
            except Exception as e:
                self.print_error(f"Failed to save: {e}")
        
        input("Press Enter to continue...")

    def search_person_by_username(self):
        """Search for a person by username across platforms."""
        self.print_header("SEARCH BY USERNAME")
        username = self.input_prompt("Enter username")
        
        if not username:
            self.print_error("Username cannot be empty")
            input("Press Enter to continue...")
            return
        
        results = []
        
        # List of major platforms to search
        platforms = [
            ("Twitter", f"https://twitter.com/{username}"),
            ("Instagram", f"https://instagram.com/{username}"),
            ("GitHub", f"https://github.com/{username}"),
            ("Reddit", f"https://reddit.com/user/{username}"),
            ("YouTube", f"https://youtube.com/@{username}"),
            ("TikTok", f"https://tiktok.com/@{username}"),
            ("Twitch", f"https://twitch.tv/{username}"),
            ("Discord", f"https://discordapp.com/users/@/{username}"),
            ("Pinterest", f"https://pinterest.com/{username}"),
            ("Snapchat", f"https://snapchat.com/add/{username}"),
            ("Steam", f"https://steamcommunity.com/search/?q={username}"),
            ("Telegram", f"https://t.me/{username}"),
        ]
        
        self.print_success(f"Profile search URLs for '@{username}':")
        for platform, url in platforms:
            print(f"  {Colors.CYAN}{platform}{Colors.ENDC}: {url}")
            results.append({"platform": platform, "url": url})
        
        print()
        
        # Manual username search with DNS/HTTP checks
        self.print_info("Attempting to verify profile existence...")
        found_count = 0
        try:
            import requests
            for platform, url in platforms:
                try:
                    resp = requests.head(url, timeout=3, allow_redirects=True)
                    if resp.status_code < 400:
                        found_count += 1
                        print(f"  {Colors.GREEN}[FOUND]{Colors.ENDC} {platform}")
                except:
                    pass
        except Exception:
            pass
        
        if found_count > 0:
            self.print_success(f"Verified {found_count} active profile(s)")
        
        print()
        
        # Option to save
        save = self.input_prompt("Save search results to database? (yes/no)").lower()
        if save == 'yes' and self.ensure_database_selected():
            try:
                db_path = self.db_dir / f"{self.current_db}.txt"
                data = json.loads(db_path.read_text())
                record = {
                    "username": username,
                    "search_type": "person_by_username",
                    "platforms": [r["platform"] for r in results],
                    "verified_count": found_count,
                    "timestamp": datetime.now().isoformat()
                }
                data["records"].append(record)
                db_path.write_text(json.dumps(data, indent=2))
                self.print_success("Search results saved to database")
            except Exception as e:
                self.print_error(f"Failed to save: {e}")
        
        input("Press Enter to continue...")

    def search_person_by_phone(self):
        """Search for phone number information."""
        self.print_header("SEARCH BY PHONE NUMBER")
        phone = self.input_prompt("Enter phone number (format: +1-555-0123 or 5550123)")
        
        if not phone:
            self.print_error("Phone number cannot be empty")
            input("Press Enter to continue...")
            return
        
        # Try TrueCaller API (requires key) or other services
        self.print_info("Phone lookup services:")
        print(f"  TrueCaller: https://truecaller.com/search/{phone.replace('-', '').replace(' ', '')}")
        print(f"  ZoomInfo: https://www.zoominfo.com/search")  
        print(f"  WhitePages: https://whitepages.com/search/Phone")
        print()
        
        self.print_info("Note: Most phone lookups require paid subscriptions or API keys")
        self.print_info("Free alternatives: Google search, social media search with phone")
        
        try:
            import requests
            # Try to get country code info
            clean_phone = ''.join(c for c in phone if c.isdigit())
            if clean_phone.startswith('1'):
                print(f"  Country: United States")
            elif clean_phone.startswith('44'):
                print(f"  Country: United Kingdom")
            print()
        except:
            pass
        
        input("Press Enter to continue...")

    def search_person_by_email(self):
        """Search for a person's social profiles using email."""
        self.print_header("SEARCH BY EMAIL (SOCIAL PROFILES)")
        email = self.input_prompt("Enter email address")
        
        if not email:
            self.print_error("Email cannot be empty")
            input("Press Enter to continue...")
            return
        
        username = email.split('@')[0]
        
        self.print_info("Searching for social profiles with this email/username...")
        print()
        
        # Common platforms
        search_urls = [
            ("Google Images", f"https://www.google.com/search?q={email}&tbm=isch"),
            ("Google People", f"https://www.google.com/search?q={email}"),
            ("Bing Search", f"https://www.bing.com/search?q={email}"),
            ("LinkedIn", f"https://www.linkedin.com/search/results/people/?keywords={email}"),
            ("GitHub", f"https://github.com/search?q={username}&type=users"),
            ("Twitter", f"https://twitter.com/search?q={email}"),
            ("Facebook", f"https://facebook.com/search/people/?q={email}"),
        ]
        
        for service, url in search_urls:
            print(f"  {Colors.CYAN}{service}{Colors.ENDC}")
            print(f"    {url}\n")
        
        input("Press Enter to continue...")

    def reverse_phone_lookup(self):
        """Perform reverse phone number lookup."""
        self.print_header("REVERSE PHONE LOOKUP")
        phone = self.input_prompt("Enter phone number")
        
        if not phone:
            self.print_error("Phone number cannot be empty")
            input("Press Enter to continue...")
            return
        
        clean_phone = ''.join(c for c in phone if c.isdigit())
        
        self.print_info("Reverse phone lookup services:")
        print(f"  TrueCaller: https://truecaller.com/search/{clean_phone}")
        print(f"  WhitePages: https://whitepages.com/phone/{clean_phone}")
        print(f"  ReversePhoneLookup: https://www.reversephonelookup.com/search?number={clean_phone}")
        print(f"  ZoomInfo: https://www.zoominfo.com/")
        print(f"  Google: https://www.google.com/search?q={clean_phone}")
        print()
        
        self.print_info("Most services require paid subscriptions")
        self.print_info("Free alternative: Try Google search or social media search")
        
        input("Press Enter to continue...")

    def main_menu(self):
        """Main application menu"""
        while True:
            self.print_header("OSINT MANAGER")
            self.print_menu([
                "Database Management",
                "Email Search (Holehe)",
                "Email Search (HaveIBeenPwned)",
                "Domain Lookup (WHOIS)",
                "DNS Lookup",
                "IP Geolocation",
                "Social media Lookback",
                "Subdomain Enumeration",
                "Person Search & OSINT",
                "Configuration",
                "Exit"
            ])

            choice = self.input_prompt("Select option")

            if choice == "1":
                self.database_menu()
            elif choice == "2":
                self.search_email_holehe()
            elif choice == "3":
                self.search_email_hibp()
            elif choice == "4":
                self.search_domain_whois()
            elif choice == "5":                
                self.lookup_dns_records()
            elif choice == "6":
                self.ip_geolocation()
            elif choice == "7":
                self.social_media_lookback()
            elif choice == "8":
                self.find_subdomains()
            elif choice == "9":
                self.person_search()
            elif choice == "10":
                self.configure_api_keys()
            elif choice == "11":
                self.print_header("GOODBYE")
                print(f"{Colors.CYAN}Thank you for using OSINT Manager{Colors.ENDC}\n")
                sys.exit(0)
            else:
                self.print_error("Invalid option")
                input("Press Enter to continue...")

    def run(self):
        """Start the application"""
        self.main_menu()


def main():
    """Application entry point"""
    manager = OSINTManager()
    manager.run()


if __name__ == "__main__":
    main()
