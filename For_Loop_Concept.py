"""
Using for loop we can iterate the value in a variable.
We can iterate list, tuple, set and dictionary values.
"""


ListOfNumbers = [1,2,3,4,5,6,7,8,9]
for number in ListOfNumbers:
    if number == 3:
        continue
    if number == 6:
        print("The number is '6' now!")
        break
    print(number)

a = [1,2,3,4]
b = ["a", "b", "c"]

for x in a:
    for y in b:
        print(x,y)

for x in a:
    pass