"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     lim_max = (2 ** 31) - 1
    #     lim_min = (-2 ** 31)
    #     if x >= 0:
    #         ans = int(str(x)[::-1])
    #         return ans if ans in range(lim_min, lim_max) else 0
    #     else:
    #         ans = -int(str(x)[::-1][0:-1])
    #         return ans if ans in range(lim_min, lim_max) else 0

    def check_overflow(self, x):

        lim_max = (2 ** 31) - 1
        lim_min = (-2 ** 31)

        if x >= lim_max:
            return True
        elif x <= lim_min:
            return True
        else:
            return False

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            res = int(str(x)[::-1])
            if self.check_overflow(res):
                return 0
            else:
                return res
        else:
            res = -int(str(x)[::-1][0:-1])
            if self.check_overflow(res):
                return 0
            else:
                return res


sl = Solution()

print(sl.reverse(x=120))
print(sl.reverse(x=123))
print(sl.reverse(x=-123))
print(sl.reverse(x=1534236469))
