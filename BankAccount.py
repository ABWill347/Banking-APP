class BankAccount:
    def __init__(self, accountNum: int, balance: float):
        self.accountNum = accountNum
        if balance < 0:
            print("Initial balance cannot be negative. Setting balance to 0.")
            self.balance = 0.0
        else:
            self.balance = balance

    def getAccountBalance(self) :
        return self.balance

    def deposit(self, amount: float) :
        if amount > 0:
            self.balance += amount
            return f"Deposit successful: You have deposited: ${amount}. New balance is: ${self.balance}"
        else:
            return "Error: Deposit amount should be positive."

    def withdraw(self, amount: float) :
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrawal successful: New balance is: ${self.balance}"
            else:
                return "Error: Insufficient funds."
        else:
            return "Error: Withdrawal amount should be positive."

    def __str__(self) :
        return f"Account Number: {self.accountNum}, Balance: {self.balance}"