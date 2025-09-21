# TASK 02
from re import search
from traceback import print_tb

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

im = list(product.items())
for i in range(len(im)):
    for j in range(i + 1, len(im)):
        if im[i][1] > im[j][1]:
            im[i], im[j] = im[j], im[i]

for k, v in im:
    print(k, v)


# TASK 14

qnt = int(input("How many bodies do u want to calculate& "))
b_en = {}

for i in range(qnt):
    mm = int(input(f"Enter the mass of thr {i+1} body: "))
    sp = int(input("Enter speed: "))

    ke = (mm*sp**2)/2
    b_en[f"body_{i+1}"] = ke

print(b_en)


# TASK 16

n = int(input("Enter size: "))

mat = []
for i in range(n):
    row = []
    for j in range(n):
        el = int(input(f"Enter element ({i})({j}): "))
        row.append(el)
    mat.append(row)

sa = 0
sb = 0

for i in range(n):
    for j in range(n):
        if i<j:
            sa += mat[i][j]
        elif i> j:
            sb += mat[i][j]

print(f"Sum above: {sa}")
print(f"Sum below^ {sb}")

# TASK 17

qq = int(input("Enter the number of files: "))
fls = []

for i in range(qq):
    fls_n = input("Enter file name: ")
    fls.append(fls_n)

exx = {}
for fl in fls:
    pos = fl.find('.')
    if pos != -1:
        ex = fl[pos+1:]
        if ex in exx:
            exx[ex] +=1
        else:
            exx[ex] = 1
    else:
        if "no ext" not in exx:
            exx["no ext"] = 0
        exx["no ext"] += 1

for ex, ct in exx.items():
    print(f"{ex}: {ct}")

# TASK 18

ee = int(input("Enter the amount of expenses: "))
expen = {}
tt = 0

for i in range(n):
    catt = input("Enter category: ")
    am = int(input("Enter price: "))
    tt += am
    if catt in expen:
        expen[catt] += am
    else:
        expen[catt] = am

if ee > 0:
    av = tt/ee
else:
    av = 0

print("Total amount:", tt)
print("Average expenditure:", av)
for catt, amt in expen.items():
    print(f"{catt}: {amt}")

# TASK 19
temps = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(7):
    t = int(input(f"Enter temp for {days[i]}: "))
    temps.append(t)

print(f"Mean temp: {sum(temps)/7}")
print(f"Max: {max(temps)}")
print(f"Min: {min(temps)}")

mmm = sum(temps)/7
for i in range(7):
    if temps[i] > mmm:
        print(days[i], ":", temps[i])
