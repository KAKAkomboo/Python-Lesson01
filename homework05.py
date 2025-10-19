# TASK 02

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

counter = make_counter()
print(counter())
print(counter())
print(counter())


# TASK 12

def lists_e(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        item1 = list1[i]
        item2 = list2[i]
        if type(item1) == list and type(item2) == list:
            if not lists_e(item1, item2):
                return False
        elif item1 != item2:
            return False
    return True

a = [1, [2, 3]]
b = [1, [2, 3]]
print(lists_e(a, b))


# TASK 13

def pow(a, b):
    if b == 0:
        return 1
    return a * pow(a, b-1)

print(pow(2 , 5))

# Task 14

def get_key(a):
    keys = []
    if type(a) != dict:
        return keys
    for k, v in a.items():
        keys.append(k)
        if type(v) == dict:
            keys += get_key(v)
    return keys

w = {"a":1, "b":{"c":2,"d":{"e":3}}}
print(get_key(w))

# TASK 15

def pass_check(password):
    def check(inp):
        return inp == password
    return check

pp = pass_check("123")
print(pp("123"))


# TASK 16

def app_fun (f, a):
    results = []
    for fun in f:
         results.append(fun(a))
    return results

f_l = [lambda x: x+1, lambda x: x*2]
val = 3
print(app_fun(f_l, val))


