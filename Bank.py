class Bank:
    def __init__(self, bankId: str, bankName: str):
        self.bankId = bankId
        self.bankName = bankName
        self.branches = []

    def addBranch(self, branch):
        self.branches.append(branch)
        return f"Branch {branch.branchName} (ID: {branch.locationId}) has been added."

    def removeBranch(self, branchId: str):
        for branch in self.branches:
            if branch.locationId == branchId:
                self.branches.remove(branch)
                return f"Branch ID: {branchId} has been removed."
        return f"Branch ID: {branchId} not found."

    def getBankId(self) :
        return self.bankId

    def getBankName(self) :
        return self.bankName

    def __str__(self):
        if not self.branches:
            return f"Bank ID: {self.bankId}, Bank Name: {self.bankName}, No branches available."
        branchDetails = ", ".join([f"{branch.branchName} (ID: {branch.locationId})" for branch in self.branches])
        return f"Bank ID: {self.bankId}, Bank Name: {self.bankName}, Branches: {branchDetails}"
