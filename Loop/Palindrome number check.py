# program to check palindrome number ....
num = int(input("enter number"))
rev=0
temp=num
while num!=0:
    b=num%10
    rev=(rev*10)+b
    num//=10
print("Reversed number is",rev)
if temp==rev:
    print(" Number is palindrome number")
else:
    print(" Number is not palindrome number")

