"""
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution(object):
    def twoSum(self, nums, target):
        # result = []
        # for index in range(0, len(nums)):
        #     for index2 in range(index + 1, len(nums)):
        #         if nums[index] + nums[index2] == target:
        #             result.append([index, index2])
        # if len(result) > 0:
        #     result = result[0]
        # return result

        result = {}
        for idx, num in enumerate(nums):
            if (target - num) in result:
                return [idx, result[target - num]]
            result[num] = idx


sl = Solution()

# print(sl.twoSum(nums=[2, 7, 11, 15], target=9))
print(sl.twoSum(nums=[3, 2, 3], target=6))
