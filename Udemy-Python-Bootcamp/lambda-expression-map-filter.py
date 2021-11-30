
# ------------------ MAP Function ------------------

def square(num):
    return num**2

my_nums = [1,2,3,4,5,6]

for item in map(square, my_nums):
    print(item)
# or
print(list(map(square, my_nums)))


def splicer(str):
    if len(str) % 2 == 0:
        return "EVEN"
    return str[0]

names = ['Andy', 'Eve', 'Sally']


print(list(map(splicer, names)))


# ------------------ FILTER Function ------------------

def check_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, nums)))

for n in filter(check_even, nums):
    print(n)


# Lambda Function

num_multy = lambda num: num * num
print(num_multy(3))


# Lambda + Map
print(list(map(lambda num: num**2, nums)))

print(list(filter(lambda num: num%2==0, nums)))

print(list(map(lambda letter: letter[0], names)))

print(list(map(lambda letter: letter[::-1], names)))