my_file = open('test.txt')
print(my_file.read())
# Hellow this is the text file
# This is the second line
# This is the third line
# this is the four line
my_file.seek(0)
print(my_file.read())
# Hellow this is the text file
# This is the second line
# This is the third line
# this is the four line
my_file.seek(0)
contents = my_file.readlines()
print(contents)
# ['Hellow this is the text file\n', 'This is the second line \n', 'This is the third line\n', 'this is the four line']

my_file.close()

# fileLocation
# Windows = open("C:\\Users\\Username\\Folder\\test.txt")
# Linux_or_Mac = open("Users/Username/Folder/test.txt")

# Best Practice 
with open('test.txt') as my_new_file:
    content = my_new_file.read()
    print(content)
    # Hellow this is the text file
    # This is the second line
    # This is the third line
    # this is the four line

# File Extra
# mode = 'r': read only
# mode = 'w': write only (overwrite files or create new)
# mode = 'a': append only (will add on to files)
# mode = 'r+': read and write
# mode = 'w+': write and read (overwrite existing files or create new)
with open('test.txt', mode='a') as myfile:
    myfile.write('\nThis is six line')

with open('test.txt') as my_new_file:
    content = my_new_file.read()
    print(content)
    # Hellow this is the text file
    # This is the second line
    # This is the third line
    # this is the four line
    # This is six line

with open('myfile.txt', mode='w') as f:
    f.write("I created this file through PYTHON!")

with open('myfile.txt') as my_new_file:
    content = my_new_file.read()
    print(content)
    # I created this file through PYTHON!
