shopping_list = []

def add_item(item):
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"Item '{item}' add")
    else:
        print(f"Item '{item}' is in list")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' removed")
    else:
        print(f"Item '{item}' didnt found in list")

def show_list():
    if not shopping_list:
        print("Shopping list is empty")
    else:
        print("Your shopping list: ")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def clear_list():
    shopping_list.clear()
    print("Shopping list clean")