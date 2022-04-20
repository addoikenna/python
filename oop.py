#!bin/python3

class Bank():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name}\nBalance: ${self.balance}"

    def deposited(self, deposite):
        self.balance = self.balance + deposite
        return f"Hello {self.name}, you deposited ${deposite} and your new balance is ${self.balance}"

    def withdrawal(self, withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw
            return f"Hello {self.name}, you withdrew ${withdraw} and your new balance is ${self.balance}"
        else:
            print("The amount you entered is bigger than your balance")


name = input("PLease enter your name:\n")
while True:
    try:
        balance = int(input("Please enter your balance:\n$"))
    except:
        print("Invalid input, please enter a number")
    else:
        break

bank = Bank(name, balance)
print(bank)

activity = input("What do you want to do?\nEnter 'D' for Deposite and 'W' for wthdrawal: ").upper()

if activity == 'D':
    deposite = int(input("Please enter the amount you want to deposite:\n$"))
    print(bank.deposited(deposite))
elif activity == 'W':
    withdraw = int(input("Please enter the amount you want to withdraw:\n$"))
    print(bank.withdrawal(withdraw))
else:
    print("Invalid Input")
