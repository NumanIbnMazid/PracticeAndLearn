# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string(a, e, i, o, u) and finally return this modified string.
# Examples
# Input: "hello*3"
# Output: Ifmmp*3
# Input: "fun times!"
# Output: gvO Ujnft!


import string


def LetterChanges(str):
    result_index_list = []
    result = []
    final_result = []
    letter_list = list(string.ascii_lowercase)
    str_list = list(str)
    for s in str_list:
        s = s.lower()
        if s in letter_list:
            if (letter_list.index(s.lower()) + 1) <= 25:
                position = letter_list.index(s.lower()) + 1
            else:
                position = 0
        else:
            position = s
        result_index_list.append(position)
    for r in result_index_list:
        if type(r)  == int:
            result.append(letter_list[r])
        else:
            result.append(r)
    for res in result:
        if res.lower() in ['a', 'e', 'i', 'o', 'u']:
            res = res.capitalize()
        final_result.append(res)
    return ''.join(final_result)


# keep this function call here
print(LetterChanges(input()))
