#class Inheritance (EmployeeData)

from oops.EmployeeData import EmployeeDetails


class EmpDetails(EmployeeDetails):

    def empName(self):
        print("This is a Emp.")

    def empName2(self):
        super().empName()


#with super() keyword you can refer to the parent class

emp = EmpDetails("Peter", 12312321, "Göteborg")

emp.empName2()
#print(emp.company) - data hiding makes it impossible to refer to that variable
emp.empCompany() # It is only possible to call on the function that has data hidden variable inside