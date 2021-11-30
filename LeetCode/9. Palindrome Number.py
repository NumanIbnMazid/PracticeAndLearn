"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        org_x = x
        res_num = 0
        if x >= 0:
            while x >= 1:
                mod = x % 10
                res_num = (res_num * 10) + mod
                x = x // 10
            if res_num == org_x:
                return True
        return False

    # def isPalindrome(self, x: int) -> bool:
    #     return True if str(x)[::-1] == str(x) else False



sl = Solution()

print(sl.isPalindrome(121))
# print(sl.isPalindrome(-121))
# print(sl.isPalindrome(10))
# print(sl.isPalindrome(-101))