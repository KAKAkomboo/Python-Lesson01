#Task 02

def val_pass(password):
    if len(password) <=8:
        return False
    h_n = False
    dd = '1234567890'
    for n in password:
        if n in dd:
            h_n = True
            break
    if h_n:
        return True
    else:
        return False

print(val_pass("Pytho2134n"))

# Task 12

def split_students_by_group(st):
    gps = {}
    for nm, gp in st.items():
        if gp not in gps:
            gps[gp] = []
        gps[gp].append(nm)
    return gps

print(split_students_by_group({"Ann": "A", "Bob": "B", "Kate": "A"}))

# TASK 13

def calculate_average_by_key(items, key):
    t = 0
    c = 0
    for item in items:
        if key in item:
            t += item[key]
            c +=1
    if c == 0:
        return 0
    return t/c

print(calculate_average_by_key([{"name":"Ann","score":80},{"name":"Bob","score":60}],"score"))

# TASK 14

