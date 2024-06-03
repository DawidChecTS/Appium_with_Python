"""
A Statements which are executed by given condition is known as Conditional statements.
if condition:
    print("If condition is true then this if statement will execute")
else:
    :print("If condition is false then else statement will execute")

Here we can use below Operators in conditional statements

1.) Comparison Operators
Equals: a==B
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

2.) Logical Operators : and, or

3.) Identity Operators such as : is, is not

4.) Membership Operators such as : in, not in
"""

a = 10
b = 5
c = 10

if a == b:
    print("A is equal to B.")
elif a < c:
    print("A is les then B.")
elif a > b:
    print("A is bigger than B")
else:
    print("A and B are not equal.")

if a > b:
    if a == c:
        print("A and C are equal.")
    else:
        print("This is Else.")
else:
    print("This is 1st else")