"""
URL: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3973/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letterMap = {
            "b": 0, "a": 1, "l": 2, "L": 3, "o": 4, "O": 5, "n": 6
        }
        counterList = [0, 0, 0, 0, 0, 0, 0]

        lPassed = False
        oPassed = False

        for i in text:
            if i == "b":
                counterList[letterMap["b"]] = counterList[letterMap["b"]] + 1
            elif i == "a":
                counterList[letterMap["a"]] = counterList[letterMap["a"]] + 1
            elif i == "l":
                if lPassed == False:
                    counterList[letterMap["l"]] = counterList[letterMap["l"]] + 1
                    lPassed = True
                else:
                    counterList[letterMap["L"]] = counterList[letterMap["L"]] + 1
                    lPassed = False
            elif i == "o":
                if oPassed == False:
                    counterList[letterMap["o"]] = counterList[letterMap["o"]] + 1
                    oPassed = True
                else:
                    counterList[letterMap["O"]] = counterList[letterMap["O"]] + 1
                    oPassed = False
            elif i == "n":
                counterList[letterMap["n"]] = counterList[letterMap["n"]] + 1
            else:
                pass

        return min(counterList)

sl = Solution()

print(sl.maxNumberOfBalloons(text="nlaebolko"))
print(sl.maxNumberOfBalloons(text="loonbalxballpoono"))
print(sl.maxNumberOfBalloons(text="leetcode"))
