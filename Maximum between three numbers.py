a=int(input("enter first number"))
b=int(input("enter second number"))    #Taking input of numbers from user
c=int(input("enter third number"))
#comparing the elements by using and operator using if-else:
if a>b and a>c:
    print(a,"is the largest among the three")
elif b>c and b>a:
    print(b,"is greatest among the three")
else:
    print(c,"is the greatest among the three")



