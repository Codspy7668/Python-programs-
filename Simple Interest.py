p=int(input("Enter Principal Amount"))
r=int(input("Enter Rate Percent"))
t=int(input("Enter time period"))
#Calculation of simple interest
S=(p*r*t)/100
print("Simple Interest is",S)
#Amount Calculation after Simple Interest
Amount=p+S
print("Amount after interest is=",Amount)
A=p*(pow((1+r/100),t))
CI=A-p
print("Compound Interest is",CI) #Compound Interest Calculation



