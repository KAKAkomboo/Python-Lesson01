from random import choice

import shopping_list
from file_handler import save_to_file, load_from_file

load_from_file()

while True:
    print("Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Clear list")
    print("5. Save list in file")
    print("6. Download list from file")
    print("7. Exit")

    choice = input("Choose option (1-7): ").strip()

    if choice == "1":
        item = input("Enter item: ").strip()
        if item:
            shopping_list.add_item(item)
        else:
            print("Item cant be empty")

    elif choice == "2":
        try:
            index = int(input("Enter number item for remove"))
            shopping_list.remove_item(index - 1)
        except ValueError:
            print("Enter NUMBER")

    elif choice == "3":
        shopping_list.show_list()

    elif choice == "4":
        shopping_list.clear_list()

    elif choice == "5":
        save_to_file()

    elif choice == "6":
        load_from_file()

    elif choice == "7":
        print("Bye")
        break

    else:
        print("Wrong choice, try again")