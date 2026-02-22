import os
import json
import platform
from datetime import datetime

class ServerManager:
    def __init__(self, data_file="data/servers.json", log_file="logs/activity.log"):
        # Ini adalah 'Ingatan' si Robot
        self.data_file = data_file
        self.log_file = log_file
        self.inventory = self._load_data()

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
        print(f"OS: {platform.system()} | Architecture: {platform.machine()}")

    def display_inventory(self):
        """Shows all registered servers."""
        print("\n=== Current Inventory ===")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for name, ip in self.inventory.items():
                print(f"- {name:15} : {ip}")

    def add_server(self):
        """Logic to add a new server with validation."""
        while True:
            name = input("Enter new server name: ").strip().lower()
            if not name:
                print("Name cannot be empty.")
                continue
            if name in self.inventory:
                print(f"Error: {name} is already registered.")
                continue
            break

        while True:
            ip = input(f"Enter IP for {name}: ").strip()
            if not ip or ip.count(".") != 3:
                print("Invalid IP format (e.g., 192.168.1.1).")
                continue
            break

        # Menyimpan ke 'ingatan' robot (self.inventory)
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
                print(f"Server {name} removed.")
        else:
            print(f"Server {name} not found.")

    def check_status(self):
        """Pings all servers in the inventory."""
        print("\n=== Checking Server Status ===")
        if not self.inventory:
            print("Nothing to check.")
            return

        for name, ip in self.inventory.items():
            # Ping command for Linux (Arch)
            response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
            status = "ONLINE" if response == 0 else "OFFLINE"
            print(f"[{name:15}] {ip:15} -> {status}")
        
        self.write_log("STATUS CHECK: Performed on all servers.")