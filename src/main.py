from manager import ServerManager

def main():

    app = ServerManager()

    while True:
        print("==== Menu Options =====")
        print("1. Add New Server")
        print("3. Check All Server Status")
        print("4. Show Inventory")
        print("5. Delete Server")
        print("6. Check System")
        print("7. Exit")

        try:
            choice = input("Select menu (1/2/3/4/5/6/7): ")
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break
        if choice == "1":
            app.add_server()
        elif choice == "3":
            app.check_status()
        elif choice == "4":
            app.display_inventory()
        elif choice == "5":
            app.delete_server()
        elif choice == "6":
            app.check_system()
        elif choice == "7":
            print("\nProgram stopped")
            break
        else:
            print("\nInvalid choice, please try again.\n")


if __name__ == "__main__":
    main()
