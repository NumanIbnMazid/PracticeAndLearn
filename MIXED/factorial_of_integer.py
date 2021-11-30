

def factorial(num):
    """
    Recursive function to find the factorial of an integer
    """
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

num = 3

print(f"The factorial of number {num} is: {factorial(num)}")