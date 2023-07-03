num=int(input("Enter the number"))
sum=0
while num!=0:
  l=num%10
  sum=sum+l
  num//=10
print("The sum of digits is",sum)