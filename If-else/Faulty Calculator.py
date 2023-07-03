# in this program we are going to design a faulty calculator which will perform the following actions:
#45*3=555, 56+9=77 and 56/6=4
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
operation=input("Enter operation addition,subtraction,multiplication or division")
if operation=='addition' or operation=='Addition':
    if num1==56 and num2==9:
        print("Result is 77")
    else:
        print("Result is",num1+num2)
elif operation=='subtraction' or operation=='subtraction':
    print("Result is",num1+num2)
elif operation=='multiplication' or operation=='Multiplication':
    if num1==45 and num2==3:
        print("Result is 555",)
    else:
        print("Result is",num1*num2)
elif operation=='division' or operation=='Division':
    if num1=='56' and num2=='6':
        print("Result is 4")
    else:
        print("Result is",num1//num2)
else:
    print("Wrong input")

