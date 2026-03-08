from manager import ServerManager

def main():

    app = ServerManager()

    while True:
        print("\n==== Menu Options =====")
        print("1. Add New Server")
        print("2. Check All Server Status")
        print("3. Show Inventory")
        print("4. Delete Server")
        print("5. Check System")
        print("6. Exit")

        try:
            choice = input("Select menu (1/2/3/4/5/6/7): ")
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break
        if choice == "1":
            app.add_server()
        elif choice == "2":
            app.check_status()
        elif choice == "3":
            app.display_inventory()
        elif choice == "4":
            app.delete_server()
        elif choice == "5":
            app.check_system()
        elif choice == "6":
            print("\nProgram stopped")
            break
        else:
            print("\nInvalid choice, please try again.\n")


if __name__ == "__main__":
    main()
