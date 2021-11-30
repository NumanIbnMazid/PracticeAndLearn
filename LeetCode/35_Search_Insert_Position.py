"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        # def binary_search(nums, low, high, target, PreMid):
            
            # if high >= low:
                
            #     mid = (high + low) // 2
                
            #     if nums[mid] == target:
            #         return mid
                
            #     elif nums[mid] > target:
            #         return binary_search(nums, low, mid - 1, target, mid)
                
            #     else:
            #         return binary_search(nums, mid + 1, high, target, mid)
            # else:
            #     return PreMid
            
            
        # pre_result = binary_search(nums, 0, len(nums) - 1, target, None)
        
        # return pre_result
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                idx = mid
                end = mid - 1
            else:
                idx = mid + 1
                start = mid + 1
        return idx
        
        
    
sl = Solution()

# print(sl.searchInsert(
#     [1, 3, 5, 7, 11, 13, 14, 15, 23], 0
# ))
# print(sl.searchInsert(
#     [1,3], 2
# ))
# print(sl.searchInsert(
#     [1, 3, 5, 6], 2
# ))
print(sl.searchInsert(
    [1, 2, 4, 6, 7], 0
))