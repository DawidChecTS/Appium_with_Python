"""
Storing the different data type values in order and Set is changeable in run time. It doesn't allow duplicate values.
Values should assign to a variable in square brackets " {} "
Ex: name_set = {1,"python, 2.3,4"}
"""

# Create the Set
MySet = {1,1.2,5,"One", "Something",1, 2,6}

# We can't insert the value in set once it is created, but we can add the values.
MySet.add("Added Value")
print(MySet)

# Length af a set
print(len(MySet))

# Remove the value from set remove(), discard(), pop()
MySet.remove(2)
print(MySet)

# discard() method
MySet.discard("Something")
print(MySet)

# pop()
MySet.pop()
print(MySet)

# Join two sets. We need to use union() method not "+" to join two sets
a = {1,2,3}
b = {4,5,6,1,2}
c = a.union(b)
print(c)

# Iterate the set using membership operator
for d in c:
    print(d)

# Find if value is present in the set using membership operator
a = 7 in c
print(a)

# Clear the data in set variable using clear() method
c.clear()
print(c)

# Delete set using del
del MySet
print(MySet)