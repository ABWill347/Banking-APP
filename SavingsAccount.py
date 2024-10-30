from BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, accountNum: int, balance: float, annualInterestRate: float = 2.5):
        super().__init__(accountNum, balance)
        self.annualInterestRate = annualInterestRate

    def get_annual_interest_rate(self):
        return self.annualInterestRate

    def get_balance_next_month(self):
        return round(self.balance * (1 + (self.annualInterestRate / 100 / 12)), 2)

    def get_compounded_balance(self, months: int):
        return round(self.balance * (1 + (self.annualInterestRate / 100 / 12)) ** months, 2)

    def __str__(self) :
        return (f"Account Number: {self.accountNum}, Balance: {self.balance}, "
                f"Annual Interest Rate: {self.annualInterestRate}%")