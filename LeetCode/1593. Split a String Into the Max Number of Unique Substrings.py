"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.
"""
# letterIndex == idx - 1

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        letters = list(s)
        ans = []
        found = False
        pre_str = "?"
        for idx, letter in enumerate(letters):
            if letter not in ans:
                ans.append(letter)
                found = False
            else:
                found = True
                # if pre_str[0] == str(idx - 1):
                if pre_str[0] == "?":
                    pre_str = str(idx) + letter
                else:
                    if pre_str[0] == str(idx - 1):
                        pre_str = pre_str + letter
                # print(pre_str)
                if found == True:
                    print(pre_str)
                    if pre_str[1:] not in ans:
                        ans.append(pre_str[1:])
                        pre_str = "?"
        result = len(ans)
        print(ans)
        return result


sl = Solution()

# print(sl.maxUniqueSplit(s="ababccc"))  # 5
# print(sl.maxUniqueSplit(s="aba")) # 2
# print(sl.maxUniqueSplit(s="aa")) # 1
# print(sl.maxUniqueSplit(s="llkcegedae"))  # 7
print(sl.maxUniqueSplit(s="wwwzfvedwfvhsww"))  # 11
