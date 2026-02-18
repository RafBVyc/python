from utils import *

inventory_data = load_data()

while True:
    print("==== Menu Options =====")
    print("1. Add New Server")
    print("2. Search Server")
    print("3. Check All Server Status")
    print("4. Show Inventory")
    print("5. Delete Server")
    print("6. Check Website")
    print("7. Exit")

    try:
        choice = input("Select menu (1/2/3/4/5/6/7): ")
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break
    if choice == "1":
        add_server(inventory_data)
    elif choice == "2":
        search_and_add_server(inventory_data)
    elif choice == "3":
        check_server_status(inventory_data)
    elif choice == "4":
        show_inventory(inventory_data)
    elif choice == "5":
        delete_server(inventory_data)
    elif choice == "6":
        check_website_input()
    elif choice == "7":
        print("\nProgram stopped")
        break
    else:
        print("\nInvalid choice, please try again.\n")