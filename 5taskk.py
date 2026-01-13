# ===== DILYAZ STYLE =====

class BankAccount:
    def __init__(self, downer, dbalance):
        self.__owner = downer
        self.__balance = dbalance   # private attribute

    def deposit(self, damount):
        self.__balance += damount

    def withdraw(self, damount):
        if damount <= self.__balance:
            self.__balance -= damount
        else:
            print("Not enough balance")

    def get_balance(self):
        return self.__balance


# Demonstration
daccount = BankAccount("Dilyaz", 100000)
daccount.deposit(20000)
daccount.withdraw(50000)

print("Balance:", daccount.get_balance())
