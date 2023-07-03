num=int(input("Enter the number"))
sum=0
flag=num
while num!=0:
  l=num%10
  sum=sum+(l)**3
  num//=10
print("The sum of cube of digits is",sum)
if flag==sum:
  print("Number is an armstrong number")
else:
  print(" Number is not an armstrong number")