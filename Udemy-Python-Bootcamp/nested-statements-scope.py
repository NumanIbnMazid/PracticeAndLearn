
x = 50

def func():
    global x
    print(f"x is : {x}")

    # Local reassignment on a Global Variable
    x = "NEW VALUE"

    print(f"I just changed Global x to : {x}")


print(x) # 50
print(func())
print(x)  # NEW VALUE
