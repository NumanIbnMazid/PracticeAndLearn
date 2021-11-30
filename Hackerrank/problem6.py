
# Problem:
    # Read an integer N.

    # Without using any string methods, try to print the following:
        # 123 ... N 

    # Note that "..." represents the values in between.

# if __name__ == '__main__':
#     n = int(input())
#     numbers = []
#     for num in range(1, n+1):
#         numbers.append(num)
#     print('{}'*len(numbers)).format(*numbers)


if __name__ == '__main__':
    n = int(input())
    print(''.join(str(x+1) for x in range(n)))
