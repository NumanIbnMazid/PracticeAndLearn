
# Task
    # Read an integer N. For all non-negative integers i < N, print i2. See the sample for details.


if __name__ == '__main__':
    n = int(input())
    for number in range(0,n):
        if number < n:
            result = number ** 2
            print(result)
