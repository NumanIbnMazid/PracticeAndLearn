

def myfunc(*args): # args treats as a tupple inside a function
    # Returns 5% of the sum
    return sum(args) * 0.05

print(myfunc(50, 30, 20, 100))
# 10.0


def myfunc2(*spam):  # args treats as a tupple inside a function
    # Returns 5% of the sum
    return sum(spam) * 0.05


print(myfunc2(50, 30, 20, 100))
# 10.0


def kwargsfunc(**kwargs):
    print(kwargs)
    # {'fruit': 'apple', 'flower': 'rose'}
    if 'fruit' in kwargs:
        return f"My fruit of choice is {kwargs['fruit']}."
    return "I didn't find any fruit here."


print(kwargsfunc(fruit='apple', flower='rose'))
# My fruit of choice is apple.


def argkwargfunc(*args, **kwargs):
    print(args)
    # (10, 20, 30)
    print(kwargs)
    # {'fruit': 'Banana', 'food': 'Eggs', 'animal': 'Dog'}
    return "I would like {} {}".format(args[0], kwargs['food'])

print(argkwargfunc(10, 20, 30, fruit='Banana', food='Eggs', animal='Dog'))
# I would like 10 Eggs
