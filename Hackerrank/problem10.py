

# Problem:
    # Given the names and grades for each student in a Physics class of N students, 
    # store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    # Note: If there are multiple students with the same grade, order their names 
    # alphabetically and print each name on a new line.

# Input Format

    # The first line contains an integer, N, the number of students.
    # The 2N subsequent lines describe each student over 2 lines
    # the first line contains a student's name, and the second line contains their grade.


# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry

# Soliution Practice:

# if __name__ == '__main__':
#     scores = []
#     results = []
#     for number in range(int(input("Enter student number:"))):
#         name = input(f"Enter student {number + 1}'s name:")
#         score = float(input(f"Enter student {number + 1}'s score:"))

#         # print(name)
#         # print(score)

#         scores.append([name, score])

#     lowest_score = min(scores, key=lambda x:x[1])

#     for scr in scores:
#         # print(scr[1])
#         if scr[1] == lowest_score[1]:
#             scores.remove(scr)
    
#     second_lowest_score = min(scores, key=lambda x: x[1])

#     # print(second_lowest_score[1])
#     for score in scores:
#         if score[1] == second_lowest_score[1]:
#             results.append(score)
#     print(results)
    
#     for result in results:
#         print(result[0])

# Solution 2:

# N = int(input())
# mini = 101
# mini2 = 102
# a = []
# for i in range(N):
#     name = input()
#     mark = float(input())
#     if mark < mini:
#         mini2 = mini
#         mini = mark
#     elif mark != mini and mark < mini2:
#         mini2 = mark
#     a.append([name, mark])
# b = [x[0] for x in a if x[1] == mini2]
# b.sort()
# for y in b:
#     print(y)


# Solution 3:

from decimal import Decimal
from itertools import groupby, islice
from operator import itemgetter

a = []
for i in range(int(input())):
  x, y = (input(), Decimal(input()))
  a.append((y, x))
a.sort()
for k, v in islice(groupby(a, key=itemgetter(0)), 1, 2):
  for x in v:
    print(x[1])
