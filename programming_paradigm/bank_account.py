class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("Insufficient balance")
        self.account_balance -= amount
        return self.account_balance
    
    def display_balance(self):
        print(f"Your account balance is: {self.account_balance}")


