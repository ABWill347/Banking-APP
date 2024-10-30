from BankAccount import BankAccount


class CheckingAccount(BankAccount):
    minBalance = 25.00
    withdrawFee = 0.25
    overdraftFee = 18.00

    def __init__(self, accountNum: int, balance: float):
        super().__init__(accountNum, balance)
        self.minBalance = float(CheckingAccount.minBalance)
        self.withdrawFee = float(CheckingAccount.withdrawFee)
        self.overdraftFee = float(CheckingAccount.overdraftFee)

        if self.balance < self.minBalance:
            print("Minimum balance for checking must be at least $25.00!")
            while self.balance < self.minBalance:
                print(f"Re-enter initial balance of at least ${self.minBalance:,.2f}: ")
                self.balance = int(input())

    def withdraw(self, amount):
        self.balance -= amount
        self.balance -= self.withdrawFee
        print(f"Amount withdrawn is ${amount:,.2f}. New balance with applied fees is ${self.balance:,.2f}")

        if self.balance < 0:
            self.balance -= self.overdraftFee
            print(f"An overdraft fee of ${self.overdraftFee:,.2f} has been applied due to negative balance!")
            print(f"Your new balance is: ${self.balance:,.2f}")

    def __str__(self) :
        return (f"Account Number: {self.accountNum}, Balance: {self.balance}, "
                f"Min Balance: {self.minBalance}, Withdraw Fee: {self.withdrawFee}, Overdraft Fee: {self.overdraftFee}")

