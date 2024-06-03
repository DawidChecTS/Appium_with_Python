# **************************** String Data Type ****************************
"""
A sequence of characters is known as string
Ex: name = "Python"
"""

# Assigning Single line string to a variable
name_1 = "Hello World"
print(name_1)

# Assigning Multi line string to a variable
name_2 = """
            This is a 
            Python Tutorial
            Hello
            World
"""
print(name_2)

#Slicing - Getting the required portion of the data in the string [1:n -1]
name_3 = name_1[0:3]
print(name_3)
name_3 = name_1[3:]
print(name_3)

#String Lenght = len()
print(len(name_3))

#Converting string to upper case = upper()

print(name_1.upper())

#Converting string to lower case = lower()

print(name_1.lower())

#Replace some the string in sentence = replace("word to take away", "word to replace with".)

print(name_1.replace("World", "Python"))

# String Concatenation " + "
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

# Find the string in a sentence using Membership operators  - (in, not in)
#If string is present in sentence then it will return "True".

name_4 = "Hey this is python tutorial."

a = "Hey" in name_4
b = "You" is not name_4
print(a)
print(b)

