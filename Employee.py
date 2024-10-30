from datetime import date


class Employee:
    idCouter = 1

    def __init__(self, empFirstName: str, empLastName: str, salary: float, startDate: date, terminationDate: date):
        self.employeeId = Employee.idCouter
        Employee.idCouter += 1
        self.empFirstName = empFirstName
        self.empLastName = empLastName
        self.salary = salary
        self.startDate = startDate
        self.terminationDate = terminationDate

    def getEmpFirstName(self):
        return "Employee First name is :", self.empFirstName

    def setEmpFirstName(self, empFirstName: str):
        self.empFirstName = empFirstName

    def getEmpLastName(self):
        return "Employee Last name is :", self.empLastName

    def setEmpLastName(self, empLastName: str):
        self.empLastName = empLastName

    def getSalary(self):
        return "Employee Salary is :", self.salary

    def setSalary(self, salary: float):
        self.salary = salary

    def getStartDate(self):
        return "Employee Start Date is :", self.startDate

    def setStartDate(self, startDate: date):
        self.startDate = startDate

    def getTerminationDate(self):
        return "Employee Termination date is :", self.terminationDate

    def setTerminationDate(self, terminationDate: date):
        self.terminationDate = terminationDate

    def getEmployeeId(self):
        return "Employee ID is :", self.employeeId

    def setEmployeeId(self, employeeId: str):
        self.employeeId = employeeId

    def nameToUpper(self):
        return self.empFirstName.capitalize()

    def lastNameToUpper(self):
        return self.empLastName.capitalize()

    def __str__(self):
        return f"Employee ID: {self.employeeId},Employee First Name and Last:{self.nameToUpper(), self.lastNameToUpper()},Employee Start Date:{self.startDate},Employee End Date:{self.terminationDate} "

