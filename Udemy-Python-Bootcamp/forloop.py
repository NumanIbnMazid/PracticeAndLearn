my_list = [(1, 2), (3, 4), (5, 6)]

for num in my_list:
    print(num)
    # (1, 2)
    # (3, 4)
    # (5, 6)

    
# Tuple Unpacking
for (a, b) in my_list:
    print(a)
    print(b)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

num_list = [1,2,3,4,5]
for _ in num_list:
    print("Hellow!")
    # Hellow!
    # Hellow!
    # Hellow!
    # Hellow!
    # Hellow!

d = {'key1': 1, 'key2': 2, 'key3': 3}

for item in d:
    print(item)
    # key1
    # key2
    # key3
for item in d.items():
    print(item)
    # ('key1', 1)
    # ('key2', 2)
    # ('key3', 3)
for key,value in d.items():
    print(value)
    # 1
    # 2
    # 3

for value in d.values():
    print(value)
    # 1
    # 2
    # 3
