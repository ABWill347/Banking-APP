from datetime import date
from BankAccount import BankAccount

class Customer:
    idCounter = 1

    def __init__(self, membershipDate: date, firstName: str, lastName: str, birthDate: date,streetAddress: str, city: str, state: str, zipcode: str, phoneNumber: str,accountNum: int, balance: float):
        self.customerID = Customer.idCounter
        Customer.idCounter += 1
        self.membershipDate = membershipDate
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.bankAccount = BankAccount(accountNum, balance)

    def get_customer_id(self) :
        return f"Customer ID: {self.customerID}"

    def get_membership_date(self) :
        return f"Membership Date: {self.membershipDate}"

    def set_membership_date(self, membershipDate: date) :
        self.membershipDate = membershipDate

    def get_first_name(self) :
        return f"First Name: {self.firstName}"

    def set_first_name(self, firstName: str) :
        self.firstName = firstName

    def get_last_name(self) :
        return f"Last Name: {self.lastName}"

    def set_last_name(self, lastName: str) :
        self.lastName = lastName

    def get_birth_date(self) :
        return f"Birth Date: {self.birthDate}"

    def set_birth_date(self, birthDate: date) :
        self.birthDate = birthDate

    def get_street_address(self) :
        return f"Street Address: {self.streetAddress}"

    def set_street_address(self, streetAddress: str) :
        self.streetAddress = streetAddress

    def get_city(self) :
        return f"City: {self.city}"

    def set_city(self, city: str) :
        self.city = city

    def get_state(self) :
        return f"State: {self.state}"

    def set_state(self, state: str) :
        self.state = state

    def get_zipcode(self) :
        return f"Zipcode: {self.zipcode}"

    def set_zipcode(self, zipcode: str) :
        self.zipcode = zipcode

    def get_phone_number(self) :
        return f"Phone Number: {self.phoneNumber}"

    def set_phone_number(self, phoneNumber: str) :
        self.phoneNumber = phoneNumber

    def deposit(self, amt: float) :
        return self.bankAccount.deposit(amt)

    def withdraw(self, amt: float) :
        return self.bankAccount.withdraw(amt)

    def getBalance(self) -> float:
        return self.bankAccount.getAccountBalance()

    def nameToUpper(self):
        return self.firstName.capitalize()

    def lastNameToUpper(self):
        return self.lastName.capitalize()

    def __str__(self) -> str:
        return (f"Customer ID: {self.customerID}\n"
                f"Membership Date: {self.membershipDate}\n"
                f"Name: {self.nameToUpper()} {self.lastNameToUpper()}\n"
                f"Birth Date: {self.birthDate}\n"
                f"Address: {self.streetAddress}, {self.city}, {self.state}, {self.zipcode}\n"
                f"Phone: {self.phoneNumber}\n"
                f"{self.bankAccount}")