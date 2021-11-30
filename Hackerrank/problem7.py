

# Task
    # You have a non-empty set s, and you have to execute N commands given in N lines.

    # The commands will be pop, remove and discard.

# Input Format

    # The first line contains integer n, the number of elements in the set s.
    # The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
    # The third line contains integer N, the number of commands.
    # The next N lines contains either pop, remove and/or discard commands followed by their associated value.


num = int(input())
data = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    data.remove(int(oper[1]))
  elif oper[0] == "discard":
    data.discard(int(oper[1]))
  else:
    data.pop()

print(sum(data))
