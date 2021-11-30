# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
# Examples
# Input: "aa6?9"
# Output: false
# Input: "acc?7??sss?3rr1??????5"
# Output: true

# import string

# def QuestionsMarks(str):
#     for s in str:
#         if s in string.digits:
#             print(s)
#     return False


import re

def QuestionsMarks(str):
    n = re.split("\d", "a"+str+"a")  # make sure it does not start/end with ?
    q = [ques for ques in n if re.match("^\?+$", ques)]
    result = f"{sum(len(qq) for qq in q) > 2}"
    return result.lower()

# keep this function call here
print(QuestionsMarks("acc?7??sss?3rr1??????5"))
# acc?7??sss?3rr1??????5
