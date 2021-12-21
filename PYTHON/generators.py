"""
There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

- Create Generators in Python
It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.

- Differences between Generator function and Normal function
Here is how a generator function differs from a normal function.

Generator function contains one or more yield statements.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.
"""

# A simple generator function


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# It returns an object but does not start execution immediately.
a = my_gen()
# We can iterate through the items using next().
next(a)
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
next(a)
next(a)
# Finally, when the function terminates, StopIteration is raised automatically on further calls.
# next(a)
# next(a)

"""
One interesting thing to note in the above example is that the value of variable n is remembered between each call.

Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore, the generator object can be iterated only once.

To restart the process we need to create another generator object using something like a = my_gen().

One final thing to note is that we can use generators with for loops directly.

This is because a for loop takes an iterator and iterates over it using next() function. It automatically ends when StopIteration is raised.
"""

# Using for loop
for item in my_gen():
    print(item)


"""
Python Generators with a Loop
The above example is of less use and we studied it just to get an idea of what was happening in the background.

Normally, generator functions are implemented with a loop having a suitable terminating condition.

Let's take an example of a generator that reverses a string.
"""


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

"""
Python Generator Expression
Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.

Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.

The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time.

They have lazy execution ( producing items only when asked for ). For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
"""

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# or
print(next(generator))

print(next(generator))

print(next(generator))

print(next(generator))

"""
- Pipelining Generators
Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator for squaring numbers.

If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way by pipelining the output of generator functions together.
"""


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x


def square(nums):
    for num in nums:
        yield num**2

print("*** fibonacci ***")
print(sum(square(fibonacci_numbers(10))))
