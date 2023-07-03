

Python code to demonstrate working of
add(), sub(), mul()

importing operator module
import operator

# Initializing variables
a = int(input("Enter the number"))

b = int(input("enter the number"))

# using add() to add two numbers
print ("The addition of numbers is :",end="");
print (operator.add(a, b))

# using sub() to subtract two numbers
print ("The difference of numbers is :",end="");
print (operator.sub(a, b))

# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))
