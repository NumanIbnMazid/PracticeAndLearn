"""
URL: https://leetcode.com/problems/longest-common-prefix/

14. Longest Common Prefix
Easy

5126

2425

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

# Not Solved

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        CommonPrefix = []
        ResultPrefix = []
        for (i, w) in enumerate(strs):
            for (k, l) in enumerate(w):
                if i == 0:
                    CommonPrefix.append(
                    {k: l}
                )
                else:
                    pass
        return CommonPrefix
    
solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))