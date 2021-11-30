"""
Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"

Example 2:

Input: s = "1001"
Output: 0

Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"

Example 4:

Input: s = "100100010100110"
Output: 12
 

Constraints:

3 <= s.length <= 10^5
s[i] is '0' or '1'.
"""


# class Solution:
#     def numWays(self, s: str) -> int:
#         raw_string = s
#         ans = 0
#         if list(s).count('1') == 3 and len(list(s)) == 3:
#             return 1
#         if list(s).count('1') <= 0:
#             s = str('1' * len(s))
#         letters = list(s)
#         num_of_1 = letters.count('1')
#         letters_length = len(letters)
#         if '1' in s:
#             div_res = int(letters_length / num_of_1)
#             return num_of_1, letters_length, div_res, raw_string
#             if (num_of_1 + div_res) % 2 != 0 and list(raw_string).count('1') > 2:
#                 return letters_length + div_res
#             if letters_length % div_res == 0 and list(raw_string).count('1') < 2:
#                 return letters_length - div_res
#             if num_of_1 >= 3:
#                return ((letters_length + div_res) - num_of_1) + 1
#             # return num_of_1, letters_length, div_res
#         return ans

import itertools


class Solution:
    def numWays(self, s: str) -> int:
        raw_string = s
        ans = 0
        letters = list(s)
        num_of_1 = letters.count('1')
        letters_length = len(letters)
        # combination_obj = itertools.combinations(letters, num_of_1)
        # combinations = list(combination_obj)
        idxs = []
        combs_holder = []
        for idx, letter in enumerate(letters):
            if letter == '1':
                idxs.append(idx + 1)
        for idx in idxs:
            combination_obj = itertools.combinations(letters, idx)
            combinations = list(combination_obj)
            combs_holder.append(combinations)
        return combs_holder


# [[('1',), ('0',), ('1',), ('0',), ('1',)], [('1', '0', '1'), ('1', '0', '0'), ('1', '0', '1'), ('1', '1', '0'), ('1', '1',
#                                                                                                                  '1'), ('1', '0', '1'), ('0', '1', '0'), ('0', '1', '1'), ('0', '0', '1'), ('1', '0', '1')], [('1', '0', '1', '0', '1')]]
sl = Solution()

print(sl.numWays(s="10101"))  # 4
# print(sl.numWays(s="100100010100110"))  # 12
# print(sl.numWays(s="1001"))  # 0
# print(sl.numWays(s="0000"))  # 3
# print(sl.numWays(s="111"))  # 1
# print(sl.numWays(s="1001001"))  # 9
# print(sl.numWays(s="00000000"))  # 21
# print(sl.numWays(s="0000"))  # 0
