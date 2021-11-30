

# class Account():

#     def __init__(self, value):
#         self.value = value

#     def add_deposit(self, amount):
#         self.value = self.value + amount
#         return f"{self.value} is your current balance."
    
#     def withdraw(self, amount):
#         if amount > self.value:
#             return "You don't have sufficient balance!"
#         else:
#             self.value = self.value - amount
#         return f"{self.value} is your current balance."

#     def choose_option(self):
#         option = input("Please enter '1' to deposit, '2' to withdraw:")
#         if option in ['1', '2']:
#             amount = int(input("Please enter the amount: "))
#             if option == '1':
#                 return self.add_deposit(amount)
#             if option == '2':
#                 return self.withdraw(amount)
#         return "Failed"




# account1 = Account(100)
# account2 = Account(500)

# print(account1.choose_option())


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')



acct1 = Account('Jose', 100)

print(acct1)

acct1.deposit(50)

print(acct1.balance)

acct1.withdraw(75)

print(acct1.balance)

