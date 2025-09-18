# TASK 02
from re import search

product = {"Apple": 12, "Banana": 15, "Tomato": 21, "Potato": 30}

p = list(product.values())

print(f"Sum = {sum(product.values())}")
print(f"Max price = {max(p)}")
print(f"Min price ={min(p)}")

# TASK 12

phones = {"Petya": 11111111,
          "Vasya": 22222222,
          "Maria": 33333333,
          "Petro": 44444444}

while True:
    print("1. Show all contacts")
    print("2/ Search contact")
    print("3. Delete contact")
    print("4. Add contact")
    print("5. Exit")

    c = int(input("Choose option: "))

    if c == 1:
        for n, c in phones.items():
            print(f"{n}: {c}")

    elif c == 2:
        sc = input("Enter name to search: ")
        if sc in phones:
            print(f"{sc}: {phones[sc]}")
        else:
            print("Contact not found")

    elif c == 3:
        d = input("Enter name to delete: ")
        if d in phones:
            del phones[d]
            print("Contact delete")
        else:
            print("Contact not found")

    elif c == 4:
        new_name = input("Enter name: ")
        new_n = input("Enter number: ")
        phones[new_name] = new_n
        print("Contact add")

    elif c == 5:
        break

    else:
        print("Try again")

# TASK 13


