from Employee import Employee
from datetime import date
from Branch import Branch
from Customer import Customer
from Bank import Bank
from CheckingAccount import CheckingAccount
bank1 =Bank(1,"General Trust")
bank2=Bank(2,"World Bank")
branch1 = Branch(bank1, 201, "Main Street")
branch2 = Branch(bank1, 202, "Second Avenue")
branch3=Branch(bank2,"NorthShore","Elliott")
employee1=Employee("TOM","Joe",3000.0,date(2010,5,20),None)
employee2=Employee("John","ron",5000.00,date(2016,1,6),None)

branch1.addEmployee(employee1)
branch1.addEmployee(employee2)
customer1=Customer(date(2024,10,29),"Tom","Lewis",date(2010,5,20),"Yellow brick road","Newark","DE","19845","22522",1111,2255.22)
customer1.withdraw(20)
customer2=Customer(date(2024,10,29),"John","Lewis",date(2010,5,20),"Yellow brick road","Newark","DE","19845","22522",1111,2255.22)

ch1=CheckingAccount(1,28.22)
print(ch1)
print(customer2)
