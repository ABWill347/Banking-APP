
class Branch:
    def __init__(self, bank, locationId, branchName):
        self.bank = bank
        self.locationId = locationId
        self.branchName = branchName
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def removeEmployee(self, employee):
        self.employees.remove(employee)

    def getLocationId(self):
        return self.locationId

    def getBranchName(self):
        return self.branchName

    def __str__(self):
        employeeDetails = ", ".join(str(emp) for emp in self.employees)
        return f"Branch Name: {self.branchName}, Location ID: {self.locationId}, Employees: [{employeeDetails}]"