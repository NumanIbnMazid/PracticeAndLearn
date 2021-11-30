my_list = ["String", 100, 100.45, True]

print(my_list)
# ['String', 100, 100.45, True]
print(len(my_list))
# 4

list_2 = ["One", "Two", "Three"]

print(list_2[0])
# One
print(list_2[1:])

list_3 = ["Four", "Five", "Six"]

print(list_2 + list_3)
# ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

new_list = list_2 + list_3
print(new_list)
# ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

new_list[0] = (new_list[0]).upper()
print(new_list)
# ['ONE', 'Two', 'Three', 'Four', 'Five', 'Six']

new_list.append('Seven')
print(new_list)
# ['ONE', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']

popped_item = new_list.pop()
print(popped_item)
# Seven
print(new_list)
# ['ONE', 'Two', 'Three', 'Four', 'Five', 'Six']

new_list.pop(0)
print(new_list)
# ['Two', 'Three', 'Four', 'Five', 'Six']

str_list = ['a', 'c', 'b', 'e', 'd']
num_list = [1, 5, 3, 6, 2, 4]
print(str_list.sort())
# None
print(num_list.sort())
# None
str_list.sort()
num_list.sort()
print(str_list)
# ['a', 'b', 'c', 'd', 'e']
print(num_list)
# [1, 2, 3, 4, 5, 6]

str_list.reverse()
print(str_list)
# ['e', 'd', 'c', 'b', 'a']
num_list.reverse()
print(num_list)
# [6, 5, 4, 3, 2, 1]

