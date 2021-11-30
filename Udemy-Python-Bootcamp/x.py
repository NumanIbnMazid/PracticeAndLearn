list1 = [1, 6, 4, 77]
list2 = [1, 6, 77]

# def check(list1, list2):
for i in list1:
    # print(i)
    if i not in list2:
        print("result:", i)

# print(check(list1, list2))