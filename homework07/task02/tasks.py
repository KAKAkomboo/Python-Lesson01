tasks_list = []

def add_task(task):
    tasks_list.append(task)
    print(f"Task '{task}' add")

def remove_task(index):
    if 0 <= index < len(tasks_list):
        removed = tasks_list.pop(index)
        print(f"Task '{removed}' removed")
    else:
        print("Wrong index")

def show_task():
    if not tasks_list:
        print("Tasks list is empty")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks_list, start=1):
            print(f"{i}. {task}")