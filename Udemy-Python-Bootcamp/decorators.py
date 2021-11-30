

def hello(name='Jose'):
    print('hello() function has been executed!')

    def greet():
        return '\t This is greet() function inside hello()!'

    def welcome():
        return "\t This is welcome() inside hello()!"

    # print(greet())
    # print(welcome())
    # print("This is the end of the hello() function!")
    print("I am going to return a function!")

    if name == 'Jose':
        return greet
    else:
        return hello


my_new_func = hello('Jose')

# hello()

print(my_new_func())


def cool():

    def super_cool():
        return "\n I am very Cool!"
    
    return super_cool


some_func = cool()

print(some_func())

# Passing function as an argument

def hello():
    return "Hi Jose!"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

print(other(hello))


# decorator

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function.")
        original_func()
        print("Some extra code after the original function.")

    return wrap_func


# def func_needs_docorator():
#     print("I want to be decorated!")


# decorated_func = new_decorator(func_needs_docorator)

# print(decorated_func())

@new_decorator
def func_needs_docorator():
    print("I want to be decorated!")


print(func_needs_docorator())

