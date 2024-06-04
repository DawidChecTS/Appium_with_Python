#class Inheritance (EmployeeData)

from oops.EmployeeData import EmployeeDetails


class EmpDetails(EmployeeDetails):
    def empName2(self):
        self.empName()


emp = EmpDetails("Peter", 12312321, "Göteborg")

emp.empName2()
print(emp.company)
