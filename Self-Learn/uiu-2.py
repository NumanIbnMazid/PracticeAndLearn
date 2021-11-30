
import datetime

# --- Question 1 ---:
def get_age():
    dob_y = int(input("Please enter your birth year: "))
    dob_m = int(input("Please enter your birth month: "))
    dob_d = int(input("Please enter your birth date: "))

    dob_pre = str(dob_d) + "-" + str(dob_m) + "-" + str(dob_y)

    today = datetime.datetime.today()
    # dob = datetime

    # print(len(str(dob_y)))

get_age()
