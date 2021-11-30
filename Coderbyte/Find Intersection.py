# Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers(also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

# For example: if strArr contains["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] the output should return "1,4,13" because those numbers appear in both strings. The array given will not be empty, and each string inside the array will be of numbers sorted in ascending order and may contain negative numbers.
# Examples
# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1, 4, 13
# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1, 9, 10



import string

def FindIntersection(strArr):
    strArr = eval(strArr)
    list_1 = strArr[0].split(', ')
    list_2 = strArr[1].split(', ')
    inters = list(set(list_1).intersection(list_2))
    # inters = list(set(list_1) ^ set(list_2))
    # inters = []
    # for item in list_1:
    #     if item in list_2 and not item in inters:
    #         inters.append(item)
    map_s = list(map(int, inters))
    if len(map_s) <= 0:
        result = 'false'
    else:
        map_d = sorted(map_s)
        print(map_d)
        result = ','.join([str(i) for i in map_d])
    return result




# def FindIntersection(strArr):

#     # code goes here
#     list1 = strArr[0].split(', ')
#     list2 = strArr[1].split(', ')
#     list3 = 'false'
#     for i in list1:
#         if i in list2:
#             if(list3 == 'false'):
#                 list3 = i
#             else:
#                 list3 = list3+','+i
#     return list3

# import ast

# def FindIntersection(strArr):
#     strArr = ast.literal_eval(strArr)
#     n_list = strArr[0].replace(' ', '').split(',')
#     o_list = strArr[1].replace(' ', '').split(',')
#     result = set(n_list).intersection(set(o_list))
#     result = list(result)
#     return ', '.join(result)
# def FindIntersection(strArr):
#     import re
#     strArr = re.findall(r'"\s*([^"]*?)\s*"', strArr)
#     n_list = strArr[0].replace(' ', '').split(',')
#     o_list = strArr[1].replace(' ', '').split(',')
#     result = set(n_list).intersection(set(o_list))
#     result = list(result)
#     return ', '.join(result)
# def FindIntersection(strArr):
#     strArr = [x.strip() for x in eval(strArr)]
#     n_list = strArr[0].replace(' ', '').split(',')
#     o_list = strArr[1].replace(' ', '').split(',')
#     result = set(n_list).intersection(set(o_list))
#     result = list(result)
#     return ', '.join(result)
# keep this function call here
# print(FindIntersection(input("Enter:")))
# print(FindIntersection('["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]'))
# print(FindIntersection('["10, 33, 46, 7, 17", "1, 2, 4, 13, 15"]'))
print(FindIntersection('["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]'))
# print(FindIntersection('["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]'))

# ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
