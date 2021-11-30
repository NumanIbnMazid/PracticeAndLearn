"""
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

 

Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
 

Constraints:

1 <= k <= s.length <= 1000
s consist of lowercase English letters.
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # strList = list(s)
        # counter = 0
        # while counter <= 1:
        #     if len(strList) <= 2:
        #         movedItem = strList.pop(k - 1)
        #         strList.append(movedItem)
        #         break
        #     else:
        #         if counter == 0:
        #             movedItem = strList.pop(0)
        #             strList.append(movedItem)
        #         else:
        #             movedItem = strList.pop(k - 1)
        #             strList.append(movedItem)
        #         counter += 1
        # return "".join(strList)

        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))


sl = Solution()
print(sl.orderlyQueue(s="cba", k=1))
print(sl.orderlyQueue(s="baaca", k=3))
print(sl.orderlyQueue(s="tk", k=1))
print(sl.orderlyQueue(s="gn", k=2))
print(sl.orderlyQueue(s="mpx", k=3)) # pxm, 
