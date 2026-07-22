# encapsulation.py

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Siri", 100000000)

account.deposit(2000)
account.withdraw(1500)

print("Current Balance:", account.get_balance())