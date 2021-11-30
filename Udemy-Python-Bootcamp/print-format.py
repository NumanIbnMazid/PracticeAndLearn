print("This is a string {}".format("INSERTED")) 
# This is a string INSERTED
print("The {} {} {}".format("fox", "brown", "quick"))  
# The fox brown quick
print("The {2} {1} {0}".format("fox", "brown", "quick"))  
# The quick brown fox
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))
# The quick brown fox

result = 100/777
print("The result is: {r:1.3f}".format(r=result))
# The result is: 0.129
print("The result is: {r:10.3f}".format(r=result)) # 10 is accountable for white space(width)
# The result is:      0.129

name = "Numan"
print(f"Hello, My name is {name}")