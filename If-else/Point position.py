x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
if x>0 and y>0:
    print("It lies in first quadrant")
    print("x lies on +ve x axis")
    print("y lies on +ve y axis")
elif x<0 and y>0:
    print("It lies in second quadrant")
    print("x lies on -ve x axis")
    print("y lies on +ve y axis")
elif x<0 and y<0:
    print("It lies in third quadrant")
    print("x lies on -ve x axis")
    print("y lies on -ve y axis")
elif x>0 and y<0:
    print("It lies in fourth quadrant")
    print("x lies on +ve x axis")
    print("y lies on -ve y axis")
elif x==0 and y==0:
    print("Point lies at origin")
else:
    print("Point is invalid")
