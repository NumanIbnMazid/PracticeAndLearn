my_set = set()

print(my_set)
# set()
my_set.add(1)
print(my_set)
# {1}
my_set.add(2)
print(my_set)
# {1, 2}
my_set.add(2)
print(my_set)
# {1, 2} Unique Valu. Sets must be unique

my_list = [1,1,1,1,1,2,2,2,3,3,3]
print(my_list)
# [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
my_list = set(my_list)
print(my_list)
# {1, 2, 3}
