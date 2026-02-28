import os
import sqlite3
import platform
from datetime import datetime

class ServerManager:
    def __init__(self, data_file="data/servers.json", log_file="logs/activity.log", db_path="data/inventory.db"):
        self.data_file = data_file
        self.log_file = log_file
        self.db_path = db_path
        # self.inventory = self._load_data()

    def _init_db(self):
        """Menjamin tabel 'servers' ada di database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS servers (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT UNIQUE NOT NULL,
                ip TEXT NOT NULL      
                )
            """)
            conn.commit()

    def _load_data(self):
        """Internal method to load JSON data."""
        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_data(self):
        """Internal method to save data to JSON."""
        with open(self.data_file, "w") as f:
            json.dump(self.inventory, f, indent=4)

    def write_log(self, message):
        """Records activity to the log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def check_system(self):
        """Displays OS and Machine Architecture."""
        print(f"\nOS: {platform.system()} | Architecture: {platform.machine()}\n")

    def display_inventory(self):
        """Shows all registered servers."""
        print("\n=== Current Inventory ===")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT name, ip FROM servers")
            rows = cursor.fetchall()
        
        if not rows:
            print("inventory is empty")
        else:
            for row in rows:
                print(f"- {row:15} : {row}")
                
    def add_server(self):
        """Logic to add a new server with validation."""
        while True:
            name = input("Enter new server name: ").strip().lower()
            if not name:
                print("\nName cannot be empty.")
                continue
            if name in self.inventory:
                print(f"\nError: {name} is already registered.")
                continue
            break

        while True:
            ip = input(f"Enter IP for {name}: ").strip()
            if not ip or ip.count(".") != 3:
                print("\nInvalid IP format (e.g., 192.168.1.1).")
                continue
            break

        self.inventory[name] = ip
        self._save_data()
        self.write_log(f"ADDED: {name} ({ip})")
        print(f"\nServer {name} added successfully.")

    def delete_server(self):
        """Removes a server from inventory."""
        name = input("Enter server name to delete: ").strip().lower()
        if name in self.inventory:
            confirm = input(f"Delete {name}? (y/n): ").lower()
            if confirm == "y":
                ip = self.inventory.pop(name)
                self._save_data()
                self.write_log(f"DELETED: {name} ({ip})")
                print(f"\nServer {name} removed.")
        else:
            print(f"\nServer {name} not found.")

    def check_status(self):
        """Pings all servers in the inventory."""
        print("\n=== Checking Server Status ===")
        if not self.inventory:
            print("Nothing to check.")
            return

        for name, ip in self.inventory.items():
            # Ping command for linux terminal
            response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
            status = "ONLINE" if response == 0 else "OFFLINE"
            print(f"[{name:15}] {ip:15} -> {status}")
        
        self.write_log("STATUS CHECK: Performed on all servers.")