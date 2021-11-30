# Consider a list(list=[]). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


test = int(input())
s = []
for _ in range(test):
    cmd = list(input().split())

    if cmd[0] == 'insert':
        s.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "append":
        s.append(int(cmd[1]))
    elif cmd[0] == "sort":
        s.sort()
    elif cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "reverse":
        s.reverse()
    elif cmd[0] == "count":
        v = s.count(int(cmd[1]))
        print(v)
    elif cmd[0] == "index":
        x = s.index(int(cmd[1]))
        print(x)

    elif cmd[0] == 'print':
        print(s)


# n = int(input())
# a = []
# for _ in range(n):
#     c = input().strip()
#     if c == 'print':
#         print(a)
#     else:
#         c = c.split()
#         if len(c) == 3:
#             getattr(a, c[0])(int(c[1]), int(c[2]))
#         elif len(c) == 2:
#             getattr(a, c[0])(int(c[1]))
#         else:
#             getattr(a, c[0])()
