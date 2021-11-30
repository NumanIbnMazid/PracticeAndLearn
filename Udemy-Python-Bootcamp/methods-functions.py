
# check dog in a string

import string
def dog_check(s):
    return 'dog' in s.lower()


print(dog_check("This is my Dog!"))
# True


# PIG LATIN word check

def check_pig_latin(word):
    first_letter = word[0]
    # vowels = ['a', 'e', 'i', 'o', 'u']
    if first_letter.lower() in "aeiou":
        word = word + 'ay'
    else:
        # word = word.replace(first_letter, "") + first_letter + 'ay'
        word = word[1:] + first_letter + 'ay'
    return word


print(check_pig_latin("apple"))
# appleay
print(check_pig_latin("word"))
# ordway


print("---------------- Check Prime Number ----------------")
# Check Prime number
def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2, num):
        if num % n == 0:
            print(num, 'is not prime')
            break
    else:  # If never mod zero, then prime
        print(num, 'is prime!')


# def is_prime(num):
#     for number in range(2, num):
#         if num % number == 0:
#             return f"{num} is not prime!"
#     return f"{num} is prime!"


is_prime(17)
# 17 is prime!


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2, 4) - -> 2
# lesser_of_two_evens(2, 5) - -> 5

def lesser(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    return max(num1, num2)

print(lesser(12, 10)) # 10
print(lesser(12, 11)) # 12


def lesser2(num1, num2):
    nums = [num1, num2]
    if num1 % 2 == 0 and num2 % 2 == 0:
        nums.sort()
    else:
        nums.sort(reverse=True)
    return nums[0]


print(lesser2(12, 10))  # 10
print(lesser2(12, 11))  # 12


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') - -> True
# animal_crackers('Crazy Kangaroo') - -> False

def animal_crackers(text):
    words = text.split(' ')
    return words[0].lower()[0] == words[1].lower()[0]


print(animal_crackers("Dog Diven"))  # True
print(animal_crackers("Crazy Kangaroo"))  # False


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20, 10) - -> True
# makes_twenty(12, 8) - -> True
# makes_twenty(2, 3) - -> False

def makes_twenty(n1, n2):
    return n1 + n2 == 20 or 20 in [n1, n2]


print(makes_twenty(20, 10)) # True
print(makes_twenty(10, 10)) # True
print(makes_twenty(2, 3)) # False


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
# old_macdonald('macdonald') - -> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'


def old_macdonald(name):
    first = name.split(name[3:])
    second = name.split(name[:3])
    return first[0].capitalize() + second[1].capitalize()


print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') - -> 'home am I'
# master_yoda('We are ready') - -> 'ready are We'

def master_yoda(text):
    words = text.split(" ")
    words.reverse()
    return " ".join(words)


print(master_yoda('I am home'))  # home am I
print(master_yoda('We are ready'))  # ready are We


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) - -> True
# almost_there(104) - -> True
# almost_there(150) - -> False
# almost_there(209) - -> True


def almost_there(n):
    return n in range(90, 110) or n in range(190, 210)


print(almost_there(104)) # True
print(almost_there(150)) # False
print(almost_there(209)) # True


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
print("---------------- Has_33 ----------------")

def has_33(nums):
    list = []
    for num in nums:
        if num == 3:
            list.append(nums.index(num))
            position = nums.index(num)
            nums.pop(nums.index(num))
            nums.insert(position, 'x')
    # return list[0] - list[1] in [1, -1]
    list.sort(reverse=True)
    last_index = list.index(list[-1])
    for item in list:
        item_index = list.index(item)
        if item_index < last_index:
            if item - list[item_index + 1] in [1, -1]:
                return True
    return False


def has_33_second(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False


# Check
print(has_33([1, 3, 3])) # True
print(has_33([1, 3, 3, 1, 3, 3, 4, 7, 3])) # True
print(has_33([3, 1, 3])) # False
print(has_33_second([1, 3, 3, 1, 3, 3, 4, 7, 3]))  # True


print("---------------- PAPER DOLL ----------------")
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') - -> 'HHHeeellllllooo'
# paper_doll('Mississippi') - -> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    result = []
    letter_list = list(text)
    for letter in letter_list:
        result.append(letter * 3)
    return ''.join(result)


# def paper_doll2(text):
#     result = ''
#     for char in text:
#         result += char * 3
#     return result

# Check
print(paper_doll('Hello'))
# HHHeeellllllooo
print(paper_doll('Mississippi'))
# MMMiiissssssiiissssssiiippppppiii


print("---------------- BLACKJACK ----------------")
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5, 6, 7) - -> 18
# blackjack(9, 9, 9) - -> 'BUST'
# blackjack(9, 9, 11) - -> 19


def blackjack(a, b, c):
    total = a + b + c
    if total <= 21:
        return total
    elif a == 11 or b == 11 or c == 11 and (total - 10) <= 21:
        return total - 10
    return "BUST"


# def blackjack2(a, b, c):

#     if sum((a, b, c)) <= 21:
#         return sum((a, b, c))
#     elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
#         return sum((a, b, c)) - 10
#     else:
#         return 'BUST'



# Check
print(blackjack(5, 6, 7)) # 18
print(blackjack(9, 9, 9))  # BUST
print(blackjack(9, 9, 11)) # 19


print("---------------- SUMMER OF 69 ----------------")
# SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶
# summer_69([1, 3, 5]) - -> 9
# summer_69([4, 5, 6, 7, 8, 9]) - -> 9
# summer_69([2, 1, 6, 9, 11]) - -> 14


def summer_69(arr):
    if not 6 in arr:
        return sum(arr)
    else:
        excpt_list = []
        items_arr = []
        for num in arr:
            if num == 6 or num == 9:
                excpt_list.append(arr.index(num))
        for item in arr:
            if arr.index(item) in range(excpt_list[0], excpt_list[1] + 1):
                items_arr.append(item)
        new_arr = list(set(arr) ^ set(items_arr))
        return sum(new_arr)
    return None


# def summer_69_two(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total

# Check
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


print("---------------- SPY GAME ----------------")
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1, 2, 4, 0, 0, 7, 5]) - -> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) - -> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) - -> False


def spy_game(nums):
    check_list = []
    for num in nums:
        if num in (0, 7):
            check_list.append(num)
    return "".join(str(v) for v in check_list) == "007"


# def spy_game2(nums):

#     code = [0,0,7,'x']
    
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
       
#     return len(code) == 1

# Check
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


print("---------------- COUNT PRIMES ----------------")
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) - -> 25
# By convention, 0 and 1 are not prime.


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

# def count_primes2(num):
#     primes = [2]
#     x = 3
#     if num < 2:  # for the case of num = 0 or 1
#         return 0
#     while x <= num:
#         for y in range(3, x, 2):  # test all odd factors up to x-1
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)
            


# Check
print(count_primes(100))


print("----------------- Just for fun -----------------")
# Just for fun, not a real problem: )
#     PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#     print_big('a')

#     out: *
#     * *
#     *****
#     * *
#     * *
#     HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
#     For purposes of this exercise, it's ok if your dictionary stops at "E".


def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****',
                5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [
        4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5], 'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('a')


print("----------------- Volume of a Sphere -----------------")
# Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as
# 4/3 * π𝑟3

import math

# def vol(rad):
#     return (4/3 * (math.pi * (rad ** 3)))


def vol(rad):
    return (4/3)*(3.14)*(rad**3)

# Check
print(vol(2))


print("\n----------------- Check Range -----------------")
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num, low, high):
    if num >= low and num <= high:
        result = f"{num} is in the range between {low} and {high}"
    else:
        result = f"{num} is not in the range between {low} and {high}"
    return result


# def ran_check(num, low, high):
#     if num in range(low, high+1):
#         print('{} is in the range between {} and {}'.format(num, low, high))
#     else:
#         print('The number is outside the range.')

# def ran_bool(num, low, high):
#     return num in range(low, high+1)


# Check
print(ran_check(5, 2, 7))
print(ran_check(1, 2, 7))
print(ran_check(2, 2, 7))


print("\n----------------- Count Upper Lower -----------------")
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String: 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output:
# No. of Upper case characters: 4
# No. of Lower case Characters: 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()

# If you feel ambitious, explore the Collections module to solve this problem!


def up_low(s):
    uppers = []
    lowers = []
    for st in s:
        if st.islower():
            lowers.append(st)
        if st.isupper():
            uppers.append(st)
    result = f"Original String: {s} \nNumber of uppercase letters: {len(uppers)} \nNumber of lowercase letters: {len(lowers)}"
    return result


# def up_low(s):
#     d = {"upper": 0, "lower": 0}
#     for c in s:
#         if c.isupper():
#             d["upper"] += 1
#         elif c.islower():
#             d["lower"] += 1
#         else:
#             pass
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", d["upper"])
#     print("No. of Lower case Characters : ", d["lower"])

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

print(up_low(s))


print("\n----------------- Unique Elements -----------------")

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List: [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]


def unique_list(lst):
    uniques = []
    for item in lst:
        if item not in uniques:
            uniques.append(item)
    return uniques


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


print("\n----------------- Multyply Numbers -----------------")
# Write a Python function to multiply all the numbers in a list.

# Sample List: [1, 2, 3, -4]
# Expected Output: -24


def multiply(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result


print(multiply([1, 2, 3, -4]))


print("\n----------------- palindrome -----------------")

# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


def palindrome(s):
    s = s.replace(' ', '')
    return s[::-1] == s


print(palindrome('helleh'))
print(palindrome('madam'))
print(palindrome('nurses'))


print("\n----------------- string is pangram or not -----------------")
# Hard:
# Write a Python function to check whether a string is pangram or not.

# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example: "The quick brown fox jumps over the lazy dog"

# import string

# def ispangram(str1, alphabet=string.ascii_lowercase):  
#     alphaset = set(alphabet)  
#     return alphaset <= set(str1.lower())


def ispangram(str1, alphabet=string.ascii_lowercase):
    for char in alphabet:
        if char not in str1.lower():
            return False
    return True


print(ispangram("The quick brown fox jumps over the lazy dog"))
