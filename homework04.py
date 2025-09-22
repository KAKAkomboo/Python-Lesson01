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