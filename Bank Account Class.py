#Q17. Bank Account Class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

# Create a BankAccount object
account = BankAccount("John Doe", 1000)

# Perform transactions
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
