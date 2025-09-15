# ЗАВДАННЯ ВІДПОВІДНО МОГО ВАРІАНТУ
# ЗАВДАННЯ 2
from traceback import print_tb

a = input("Enter number: ")

if a == a[::-1]:
    print(f"{a} is palindrome")
else:
    print(f"{a} isnt palindrome")

# ДОДАТКОВІ ЗАВДАННЯ
# ЗАВДАННЯ 12

n = int(input("Enter number: "))
f = 1
for i in range(1, n+1):
    f*=i
print(f"factorial = {f}")

# ЗАВДАННЯ 13

n = int(input("Enter number: "))
s = 0
for i in range(n):
    s+=i

# ЗАВДАННЯ 14

n = int(input("Enter number: "))

for i in range(1, n+1):
    if n%i == 0:
        print(i)

# ЗАДВАННЯ 15

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

c =1
for i in range(b):
    c*=b
print(c)

# ЗАВДАННЯ 16
a = int(input("Enter width: "))
b= int(input("Enter height: "))

for i in range(b):
    c = ""
    for o in range(a):
        if i == 0 or i == b -1 or o == 0 or o == a-1:
            c+="*"
        else:
            c+=" "
    print(c)

# ЗАВДАННЯ 17

p = "111"

while True:
    a = input("Enter password: ")
    if a == p:
        print("Password is correct")
        break
    else:
        print("Wrong password")

# ЗАВДАННЯ 18

n = int(input("Enter number: "))

for i in range(n, 0,-1):
    if i%2 == 0:
        print(i)

# ЗАВДАННЯ 19

n = int(input("Enter height: "))

for i in range(1, n+1):
    print("*"*i)

# ЗАВДАННЯ 20

n = int(input("Enter number of a month: "))

m = "unknown"
d = 0

match n:
    case 1:
        m, d = "January", 31
    case 2:
        m, d = "February", 28
    case 3:
        m, d = "March", 31
    case 4:
        m, d = "April", 30
    case 5:
        m, d = "May", 31
    case 6:
        m, d = "June", 30
    case 7:
        m, d = "July", 31
    case 8:
        m, d = "August", 31
    case 9:
        m, d = "September", 30
    case 10:
        m, d = "October", 31
    case 11:
        m, d = "November", 30
    case 12:
        m, d = "December", 31

if m != "unknown":
    print("Month %d is %s and it has %d days" % (n, m, d))
else:
    print("Wrong month number")
