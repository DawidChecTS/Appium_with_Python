"""
Types of function : Non-parameter function, parameter function, return type function

Using "def" keyword we will create the function.
Function name should be in camel case (First letter should be capital from 2nd word)

def functionName():
    pass
"""


# Non-parameter function
def methodOne():
    print("This is method one")


methodOne()


# Parameter function
def methodTwo(name):
    print("This is a", name)


methodTwo("Python Tutorial.")


# Return type function
def sumOfTwoNumbers(a, b):
    c = a + b
    return c


d = sumOfTwoNumbers(4, 9)
print(d)


# Default value in function
def sumOfTwoNumbers(a, b=19):
    c = a + b
    return c


d = sumOfTwoNumbers(21)
print(d)


# Pass list to the function
def listValue(a):
    for x in a:
        print(x)


b = [1, 2, 3, 4, 5, 7, 7, 8, 8, 7, 5, 4, 4, 123]

listValue(b)


# Key and value as an argument
def methodWithKeyAndValue(name, number, address):
    print("Name:", name)
    print("Age:", number)
    print("Address:", address)


methodWithKeyAndValue(address="Salviatorget", number=12, name="TheWeed")

# Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. 
"""


def arbitraryKeywordArgumentsMethod(**kwargs):
    print(kwargs)


arbitraryKeywordArgumentsMethod(address="Salviatorget", number=12, name="TheWeed", justnumber=123)


def emptyMethod():
    pass