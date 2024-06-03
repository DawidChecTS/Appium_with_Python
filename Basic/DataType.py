"""
What is Data type?
Type of data or value is known as data type.

In python there are 5 types of data types
1. Numbers (integers, float and complex)
2. Strings
3. Lists
4. Tuple
5. Dictionary

By using type() method we can find the type of a variable
Ex : a = 5
print (type(a))
Output as: <class 'init'>

"""

#********************************* 1. Numbers Data Type ******************************************
a = 5
b = 5.2
c = 5j

print(type(a))
print(type(b))
print(type(c))

#********************************* 2.String Data Type ********************************************
"""
A sequence of characters is known as string
Ex: name = "Python"

"""

name = "Dawid"
print(type(name))

#********************************* 3. List Data type *********************************************
"""
- Storing the different data type values in order and list is changeable in run time. It allows duplicate values
- values should assign to a variable in square brackets "[]"
Ex : name_list = [1, "python", 2.3, 4]
"""

name_list = [1, "python", 2.2,1]

print(name_list)
print(type(name_list))

name_list[1] = "Changed value"
print(name_list)

#********************************* 4. Tuple Data Type *********************************************
"""
- Storing the different data type values in order and tuple is unchangeable in run time. It allows duplicate values
- values should assign to a variable in "()"
Ex : name_tuple = (1, "python", 2.3, 1)
"""

name_tuple = (1, "python", 2.3, 1)
print(name_tuple)
print(type(name_list))

#name_tuple[1] = "try to change value"


#********************************* 5. Dictionary Data Type ****************************************
"""
- Dictionaries are the key and value pairs. Which are written  with curly brackets. " { } "
Ex:

employeeData = {
"name": "Anil",
"number": "38383774"
"DOB": 1990 
}
"""
employeeData = {
    "name": "Anil",
    "number": "38383774",
    "DOB": 1990
}

print(employeeData)
print(type(employeeData))
print(employeeData["name"])