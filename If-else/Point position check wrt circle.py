r=int(input("Enterht e radius of circle"))
#Taking input of coordinates of centre of circle
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))

#Taking the coordinates of the arbitrary point
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
d=((a-x)**2-(y-b)**2)**0.5
print("Distance between points is ",int(d))
if d>r:
    print("The point lies outside the circle")
elif d==r:
    print("The point lies on the circle")
elif d<r:
    print("Point lies inside the circle")
else:
    print("Invalid input")
