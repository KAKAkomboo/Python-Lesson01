import shopping_list

def save_to_file(filename="shoppinf_list.txt"):
    try:
        with open(filename, "w") as file:
            for item in shopping_list:
                file.write(item + "\n")
        print(f"List save in file '{filename}")
    except Exception as e:
        print(f"Error")

def load_from_file(filename="shoppinf_list.txt"):
    try:
        with open(filename, "r") as file:
            shopping_list.clear()
            for line in file:
                item = line.strip()
                if item:
                    shopping_list.append(item)
        print(f"List download from file '{filename}'")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Download error")
