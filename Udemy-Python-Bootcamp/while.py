
x = 0
while x < 4:
    print(f'The value of x is: {x}')
    # x = x+1
    x += 1
else:
    print("x is not less than four")

    # The value of x is: 0
    # The value of x is: 1
    # The value of x is: 2
    # The value of x is: 3
    # x is not less than four

mystring = "Numan"
for letter in mystring:
    if letter == "m":
        continue # Goes to the top of the closest enclosing loop
    print(letter)
    # N
    # u
    # a
    # n

for letter in mystring:
    if letter == "m":
        break  # Breaks out of the current closest enclosing loop
    print(letter)
    # N
    # u

for letter in mystring:
    pass # Does nothing

