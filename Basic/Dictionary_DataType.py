"""
Dictionaries are the key and value pairs. Which are written with curly brackets. " { } "
Ex :

employeeData = {
    "name": "Dawid",
    "number": "960415",
    "DOB": "1996"
}
"""

# Create a dictionary

MyDictionary = {
    "ProductName": "ComputerDell",
    "ProductID": "11234",
    "ProductPrice": "3999"
}

# Access the value from dictionary.
print(MyDictionary["ProductName"])
print(MyDictionary["ProductID"])
print(MyDictionary["ProductPrice"])

# Update or change the value

MyDictionary["ProductName"] = "ComputerApple"
print(MyDictionary)

# Add key and value for existing dictionary
MyDictionary["Location"] = "1A"
print(MyDictionary)

# Length of a dictionary
print(len(MyDictionary))

# Copy the dictionary to other variable
DuplicatedDict = MyDictionary.copy()
print(DuplicatedDict)

# Iterate the values in dictionary
for a in MyDictionary.keys():
    print(MyDictionary[a])

# Iterate both keys and values
for a,b in MyDictionary.items():
    print(a, b)

# Remove the value
MyDictionary.pop("Location")
print(MyDictionary)

#Clear the Dictionary
MyDictionary.clear()
print(MyDictionary)

# Delete dictionary
del MyDictionary
#print(MyDictionary)


