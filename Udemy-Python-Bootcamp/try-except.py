

def ask_for_int():
    number = None
    while True:
        try:
            number = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number!")
            continue
        else:
            print("Thank you!")
            break
        finally:
            print("I always run end of try/except/else.")
    return "Number is {}".format(number)

print(ask_for_int())