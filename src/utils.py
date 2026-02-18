import platform
import os
import json 
from datetime import datetime

# Kode Warna ANSI
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"  # Reset to normal color
BOLD = "\033[1m"


# Function to check operating system and architecture
def check_system():
    print(f"OS: {platform.system()} | Architecture: {platform.machine()}")

# Function to check website status
def check_websites(website_list):
    for site in website_list:
        response = os.system(f"ping -c 1 {site} > /dev/null 2>&1")
        if response == 0:
            print(f"Website {site} Online")
        else:
            print(f"Website {site} Offline")

# Function to load server data from JSON file
def load_data():
    try:
        with open("data/servers.json", "r") as f:
            servers = json.load(f)
    except FileNotFoundError:
        servers = {}
    return servers

    
# Function to save server data to JSON file
def save_data(data):
    with open("data/servers.json", "w") as f:
        json.dump(data, f, indent=4)
        

# Function to add a new server
def add_server(data):
    while True:
        new_name = input("Enter new server name: ").strip().lower()
        if not new_name:
            print("Server name cannot be empty. Please try again.")
            continue
        if new_name in data:
            print(f"\nERROR: Server with name {new_name} is already registered with IP {data[new_name]}.")
            continue
        break

    while True:
        new_ip = input(f"Enter IP for {new_name}: ").strip()
        if not new_ip:
            print("IP cannot be empty. Please try again.")
            continue
        if new_ip.count(".") != 3 :
            print("Invalid IP format. Make sure it is like 192.168.1.1")
            continue
        if new_ip in data.values():
            for name, ip in data.items():
                if ip == new_ip:
                    print(f"\n ERROR: IP {new_ip} is already registered for server {name}.")
                    break
            continue
        break

    data[new_name] = new_ip
    save_data(data)
    write_log(f"Added new server: {new_name} with IP {new_ip}")
    print(f"\nServer {new_name} with IP {new_ip} has been saved successfully.")


# Function to search for a server and add it if not found
def search_and_add_server(data):
    print("\n=== Search ===")
    search = input("Type the server name to check: ").strip().lower()

    if search in data:
        print(f"\nFound, IP of {search} is {data[search]}\n")   
    else:
        print(f"Sorry, {search} is not registered in the server list...")
        add_now = input("Do you want to add it now? (y/n): ")
        if add_now == "y":
            additional_ip = input(f"Enter IP for {search}: ")
            data[search] = additional_ip
            save_data(data)
            write_log(f"Added new server: {search} with IP {additional_ip}")
            print(f"\nServer {search} has been added...\n")
        else:
            print("Okay, not adding it.\n")

# Function to display server inventory
def show_inventory(data):
    print("=== Current Inventory ===")
    for name, ip in data.items():
        print(f"- {name} : {ip}")

# Function to delete a server from inventory
def delete_server(data):
    print("\n=== DELETE SERVER ===")
    name_to_delete = input("Enter the server name to delete: ").strip().lower()
    if name_to_delete in data:
        server_ip = data[name_to_delete]
        confirm = input(f"Are you sure you want to delete server {name_to_delete} (y/n): ")
        if confirm.lower() == "y":
            del data[name_to_delete]
            save_data(data)
            write_log(f"Server {name_to_delete} with IP {server_ip} deleted.")
            print(f"\nServer {name_to_delete} has been deleted.\n")
        else:
            print("Deletion cancelled.\n")
    else:
        print(f"\nServer {name_to_delete} not found in inventory.\n")

# Function for logging
def write_log(message):
    # Get current time in format: Year-Month-Day Hour:Minute:Second
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write to activity.log file
    with open("activity.log", "a") as f:
        f.write(f"[{current_time}] {message}\n")

# Function to check website status by user input
def check_website_input():
    website = input("\nEnter the website to check (e.g., google.com): ")
    response = os.system(f"ping -c 1 {website} > /dev/null 2>&1  ")

    STATUS = "ONLINE" if response == 0 else "OFFLINE"

    print(f"{website}: {STATUS}")

# Function to check or ping servers
def check_server_status(inventory):
    print("\n=== CHECKING SERVER STATUS ===")

    if not inventory:
        print(f"{YELLOW}Inventory is empty, nothing to check{RESET}")
        return
    
    for name, ip in inventory.items():
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

        if response == 0:
            status = f"{GREEN}ONLINE / UP{RESET}"
        else:
            status = f"{RED}OFFLINE / DOWN{RESET}"

        print(f"[{BOLD}{name:15}{RESET}] {ip:15} -> {status}")        
    
    write_log("CHECK: Performed status check on all servers.")

