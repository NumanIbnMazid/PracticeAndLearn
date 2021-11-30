"""
https://leetcode.com/contest/biweekly-contest-34/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.
 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
Example 4:

Input: arr = [1]
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""

from typing import List

# class Solution:
#     def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
#         prevs = []
#         prevs_2 = []
#         for i1 in range(0, len(arr)):
#             if len(arr) == 2 and arr[i1] < arr[i1 + 1]:
#                 return 0
#             if len(arr) == 2 and arr[i1] > arr[i1 + 1]:
#                 return 1
#             for i2 in range(i1 + 2, len(arr)):
#                 if arr[i2] < arr[i2-1]:
#                     if not i2 in prevs:
#                         prevs.append(i2)
#                     if not i2 - 1 in prevs:
#                         prevs.append(i2 - 1)

#         res = prevs

#         # arr.reverse()

#         # for i1 in range(0, len(arr)):
#         #     for i2 in range(i1 + 2, len(arr)):
#         #         if arr[i2] > arr[i2-1]:
#         #             if not i2 in prevs_2:
#         #                 prevs_2.append(i2)
#         #             if not i2 - 1 in prevs_2:
#         #                 prevs_2.append(i2 - 1)
#         # rev_eles = []
#         # for_eles = []
#         # for ele in prevs_2:
#         #     rev_eles.append(arr[ele])
#         # arr.reverse()
#         # for ele in prevs:
#         #     for_eles.append(arr[ele])

#         # res = len(for_eles)
        
#         return res


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        idxs = []
        breakpoints = []
        new_arrs = []
        for idx, num in enumerate(arr):
            # print(idx, idx + 1 if idx + 1 <= len(arr) - 1 else len(arr) - 1)
            if arr[idx] > arr[idx + 1 if idx + 1 <= len(arr) - 1 else len(arr) - 1]:
                idxs.append(idx)
            else:
                new_arrs.append([idx])
        return idxs, new_arrs


sl = Solution()

print(sl.findLengthOfShortestSubarray(arr=[1, 2, 3, 10, 4, 2, 3, 5]))  # 3
# print(sl.findLengthOfShortestSubarray(arr=[5, 4, 3, 2, 1])) # 4
# print(sl.findLengthOfShortestSubarray(arr=[1, 2, 3]))  # 0
# print(sl.findLengthOfShortestSubarray(arr=[1]))  # 0
# print(sl.findLengthOfShortestSubarray(arr=[2, 1]))  # 1
# print(sl.findLengthOfShortestSubarray(arr=[1, 2]))  # 0
print(sl.findLengthOfShortestSubarray(arr=[2, 2, 2, 1, 1, 1]))  # 3
