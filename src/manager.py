import os
import sqlite3
import platform
from datetime import datetime

class ServerManager:
    def __init__(self, data_file="data/servers.json", log_file="logs/activity.log", db_path="data/inventory.db"):
        self.data_file = data_file
        self.log_file = log_file
        self.db_path = db_path
        self._init_db()  # Ensure DB and table are initialized
        # self.inventory = self._load_data()

    def _init_db(self):
        """Ensire 'servers' table available in database"""
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

    def _get_all_servers(self):
        """Internal method to load JSON data."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT name, ip FROM servers")
            return cursor.fetchall()

    def write_log(self, message):
        """Records activity to the log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def check_system(self):
        """Displays OS and Machine Architecture."""
        print(f"\nOS: {platform.system()} | Architecture: {platform.machine()}\n")

    def display_inventory(self):
        print("\n=== Current Inventory ===")
        rows = self._get_all_servers()
        
        if not rows:
            print("inventory is empty")
        else:
            for name, ip in rows:
                print(f"- {name:15} : {ip}")
                
    def add_server(self):
        """Logic to add a new server with validation."""
        while True:
            new_name = input("Enter new server name: ").strip().lower()
            if not new_name:
                print("\nName cannot be empty.")
                continue
            break

        while True:
            new_ip = input(f"Enter IP for {new_name}: ").strip()
            if not new_ip or new_ip.count(".") != 3:
                print("\nInvalid IP format (e.g., 192.168.1.1).")
                continue
            break

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO servers (name, ip) VALUES (?, ?)", (new_name, new_ip))
                conn.commit()

            print(f"\nServer {new_name} added successfully to database.")
            self.write_log(f"ADDED: {new_name} ({new_ip})")

        except sqlite3.IntegrityError:
            print(f"Error: Server {new_name} already exists in database!")

    def delete_server(self):
        """Removes a server from inventory."""
        del_name = input("Enter server name to delete: ").strip().lower()
        confirm = input(f"Delete {del_name}? (y/n): ").lower()
        if confirm == "y":
            try:
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM servers WHERE name = ?", (del_name,))

                    if cursor.rowcount > 0:
                        conn.commit()
                        print(f"\nServer '{del_name}' deleted successfully.")
                        self.write_log(f"DELETED: {del_name}")
                    else:
                        print(f"\nError: Server '{del_name}' not found in database.")

            except sqlite3.Error as e:
                print(f"Database error: {e}")

    def check_status(self):
        """Pings all servers in the inventory."""
        print("\n=== Checking Server Status ===")
        rows = self._get_all_servers()

        if not rows:
            print("Nothing to check. Add a server first")
            return

        for new_name, new_ip in rows:
            # Ping command for linux terminal
            response = os.system(f"ping -c 1 -W 1 {new_ip} > /dev/null 2>&1")
            status = "ONLINE" if response == 0 else "OFFLINE"
            print(f"[{new_name:15}] {new_ip:15} -> {status}")
        
        self.write_log("STATUS CHECK: Performed on all servers.")