#Creating of a class object
class EmployeeDetails:
    _company = "XYZ"

    #Data Hiding with _
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def empDetails(self, name, number, address):
        print("name:", name)
        print("Number:", number)
        print("Address:", address)

    def empName(self):
        print("Employee's name is: ", self.name)

    def empNum(self):
        print("Employee's number is: ", self.number)

    def empAddress(self):
        print("Employee's address is: ", self.address)

    def empCompany(self):
        print("This is a company:", self._company)


emp = EmployeeDetails("Dawid", 13, "Salviatorget")

#emp.empDetails("Michael", 15, "Alle")

#emp.empName()
#emp.empNum()
#emp.empAddress()
