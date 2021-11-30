"""
URL: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3960/

You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].

 

Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
Example 2:

Input: nums = [0,1,2]
Output: 1
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] < nums.length
All the values of nums are unique.
"""


class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        # store = []
        # counter = 0
        # for i, j in enumerate(nums):
        #     if i == 0:
        #         store.append(j)
        #         counter += 1
        #     else:
        #         if not nums[store[counter - 1]] in store:
        #             store.append(nums[store[counter - 1]])
        #             counter += 1
        #         else:
        #             break
        # return len(store)

        seen = [False] * len(nums)
        maximum = 0

        for i in range(len(nums)):
            if seen[i]:
                continue

            total = 1
            seen[i] = True
            k = nums[i]

            while not seen[k]:
                total += 1
                seen[k] = True
                k = nums[k]

            maximum = max(maximum, total)
            if maximum >= len(nums) / 2:
                return maximum
        return maximum

sl = Solution()

print(sl.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
print(sl.arrayNesting([0, 1, 2]))
print(sl.arrayNesting([0, 2, 1]))
