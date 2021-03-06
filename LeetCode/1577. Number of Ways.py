"""
Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
 

Example 1:

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 
Example 2:

Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
Example 3:

Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
Output: 2
Explanation: There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
Example 4:

Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
Output: 0
Explanation: There are no valid triplets.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5
"""




import itertools

def numTriplets(nums1, nums2):
    # counter = 0
    # # assign
    # all_combinations_1, all_combinations_2 = [], []
    # combinations_object_1, combinations_object_2 = itertools.combinations(
    #     nums1, 2), itertools.combinations(nums2, 2)
    # combinations_list_1, combinations_list_2 = list(
    #     combinations_object_1), list(combinations_object_2)
    # all_combinations_1 += combinations_list_1
    # all_combinations_2 += combinations_list_2
    # for num1 in nums1:
    #     for comb2 in combinations_list_2:
    #         if num1**2 == comb2[0] * comb2[-1]:
    #             counter += 1

    # for num2 in nums2:
    #     for comb1 in combinations_list_1:
    #         if num2**2 == comb1[0] * comb1[-1]:
    #             counter += 1

    # squared_numbers_1 = [number ** 2 for number in nums1]
    # squared_numbers_2 = [number ** 2 for number in nums2]
    counter = 0
    dict_1 = {}
    dict_2 = {}
    for n1 in range(0, len(nums2)):
        for n2 in range(n1 + 1, len(nums2)):
            if nums2[n1] * nums2[n2] in dict_1:
                dict_1[nums2[n1] * nums2[n2]] = dict_1[nums2[n1] * nums2[n2]] + 1
            else:
                dict_1[nums2[n1] * nums2[n2]] = 1
    for n in nums1:
        if n ** 2 in dict_1:
            counter += dict_1[n ** 2]
    # check
    for n1 in range(0, len(nums1)):
        for n2 in range(n1 + 1, len(nums1)):
            if nums1[n1] * nums1[n2] in dict_2:
                dict_2[nums1[n1] * nums1[n2]] = dict_2[nums1[n1] * nums1[n2]] + 1
            else:
                dict_2[nums1[n1] * nums1[n2]] = 1
    for n in nums2:
        if n ** 2 in dict_2:
            counter += dict_2[n ** 2]

    return counter


# print(numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9]))
# print("XXXXX")
print(numTriplets(nums1=[1, 1], nums2=[1, 1, 1]))
