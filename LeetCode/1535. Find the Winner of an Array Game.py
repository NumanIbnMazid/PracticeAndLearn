"""
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.

Example 3:

Input: arr = [1,9,8,2,3,7,6,4,5], k = 7
Output: 9

Example 4:

Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
Output: 99
 

Constraints:

2 <= arr.length <= 10^5
1 <= arr[i] <= 10^6
arr contains distinct integers.
1 <= k <= 10^9
"""
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_list = [0, 0]
        # while win_list[-1] < k:
        for element in arr:
            if win_list[-1] < k:
                check_list = [arr[0], arr[1]]
                if check_list[0] > check_list[1]:
                    lost_ele = check_list[1]
                    if check_list[0] != win_list[0]:
                        win_list = [check_list[0], 1]
                    else:
                        win_list = [check_list[0], win_list[1] + 1]
                    arr.pop(1)
                    arr.append(lost_ele)
                    # print(arr)
                else:
                    # print(check_list)
                    lost_ele = check_list[0]
                    if check_list[1] != win_list[0]:
                        win_list = [check_list[1], 1]
                    else:
                        win_list = [check_list[1], win_list[1] + 1]
                    arr.pop(0)
                    arr.append(lost_ele)
                    # print(arr)
            else:
                break
        # print(win_list)
        if win_list[-1] < k:
            # result = k // win_list[0]
            result = win_list[0]
        else:
            result = win_list[0]
        return result




# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#         winarr = arr[0]
#         w = 0
#         for x in arr[1:]:
#           if x > winarr:
#             winarr, w = x, 0
#           w += 1
#           if w == k: break
#         return winarr


sl = Solution()

print(sl.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2))  # 5
print(sl.getWinner(arr=[3, 2, 1], k=10)) # 3
print(sl.getWinner(arr=[1, 9, 8, 2, 3, 7, 6, 4, 5], k=7)) # 9
print(sl.getWinner(arr=[1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000))  # 99
