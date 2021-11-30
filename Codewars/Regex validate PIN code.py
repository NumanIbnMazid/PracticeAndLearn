# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# eg:

# validate_pin("1234") == True
# validate_pin("12345") == False
# validate_pin("a234") == False


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# def validate_pin(pin):
#     try:
#         return len(pin) in [4, 6] and type(int(pin)) == type(1) and int(pin) >= 0
#     except:
#         return False

# def validate_pin(pin):
#     result = False
#     if len(pin) in [4, 6]:
#         for p in pin:
#             if p in ['0','1','2','3','4','5','6','7','8','9']:
#                 result = True
#             else:
#                 result = False
#     return result


print(validate_pin("12345"))
print(validate_pin("123456"))
print(validate_pin("1234"))
print(validate_pin("1234r"))
print(validate_pin("123"))
print(validate_pin("123+"))
