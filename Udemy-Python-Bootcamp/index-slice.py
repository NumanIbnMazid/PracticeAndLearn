print("Hello World!")
mystring = "Hello World"
# Indexing
print(mystring[0])  # H
print(mystring[-2]) # l

mystring2 = "abcdefghijk"
print(mystring2[2:]) # cdefghijk
print(mystring2[:3])  # abc
print(mystring2[3:-5])  # def
print(mystring2[3:6])  # def
print(mystring2[::])  # abcdefghijk
# Step Slicing
print(mystring2[::2])  # acegik 
print(mystring2[2:7:2])  # ceg
# Reverse String by slicing
print(mystring2[::-1])  # kjihgfedcba
