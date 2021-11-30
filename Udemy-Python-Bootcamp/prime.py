number = int(input("Enter number:"))

def is_prime(number):
    if number == 1:
        return "Not Prime"
    elif number == 2:
        return "Prime"
    else:
        # num = 2
        for num in range(2, number):
            if number % num == 0:
                return "Not Prime"
                break
        return "Prime"
    return "Not Prime"


print(is_prime(number))

# num = 15
# if num > 1:
#     for i in range(2, num//2):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#         else:
#             print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


# Solution


# num = int(input("Enter number:"))
# if num > 1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
# else:
#    print(num,"is not a prime number")