import tasks
from utils import dis_menu

while True:
    dis_menu()
    choice = input("Choose option (1-4): ").strip()

    if choice == "1":
        new_task = input("Enter new task: ").strip()
        if new_task:
            tasks.add_task(new_task)
        else:
            print("Task cant be empty")

    elif choice == "2":
        try:
            index = int(input("Enter number task: "))
            tasks.remove_task(index - 1)
        except ValueError:
            print("Enter NUMBER")

    elif choice == "3":
        tasks.show_task()

    elif choice == "4":
        print("Bye")
        break

    else:
        print("Wrong choice, try again")