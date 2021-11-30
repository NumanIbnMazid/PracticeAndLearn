
# Problem:
    # Given the participants' score sheet for your University Sports Day, 
    # you are required to find the runner-up score. You are given n scores. 
    # Store them in a list and find the score of the runner-up.

# Input Format

    # The first line contains n. The second line contains an array A[] of n integers each separated 
    # by a space.

# Sample Input 0

# 5
# 2 3 6 6 5

# Sample Output 0

# 5

# if __name__ == '__main__':
#     n = int(input())
#     # arr = map(int, input().split())
#     arr = [2, 3, 6, 6, 5]

#     champion = []
#     runnerup = []

#     highest = max(arr)
#     champion.append(highest)
#     for score in arr:
#         if score == highest:
#             arr.remove(score)
#     arr.remove(max(arr))
#     runnerup.append(max(arr))

#     print(' '.join(map(str, champion)))    
#     print(' '.join(map(str, runnerup)))


# n = int(input())
# numb = input()
# lis = list(map(int, numb.split()))
# big, sbig = -6000, -6000
# for i in lis:
#     if (i > big):
#         big, sbig = i, big
#     elif (i < big and i > sbig):
#         sbig = i
# print(sbig)


# def max(l):
#     return sorted(set(l))[-2]


# test = int(input())
# l = [int(_) for _ in input().split()]
# print(max(l))


n = int(input())
a = map(int, input().strip().split(" "))
a = list(a)
mx1 = a[0]
mn = a[0]
for i in a:
    if(i > mx1):
        mx1 = i
    if(i < mn):
        mn = i
mx2 = mn
for i in a:
    if(i > mx2 and i < mx1):
        mx2 = i
print(mx2)
