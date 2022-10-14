class Employee:
    employeeId = None
    eName = None

    def __init__(self, eId, eN):
        self.employeeId = eId
        self.eName = eN

    def output(self):
        print(self.employeeId, self.eName)


ob = Employee(1, 'Anjana')
ob.output()
