#program to print gross salary of an employee..
salary=int(input('Enter Basic Salary'))
if salary<=10000:
    print("Your basic salary is",salary)
    print("Your HRA is",0.2*salary)
    print("Your DA is",0.8*salary)
    print("Gross Salary is ",salary+0.2*salary+0.8*salary)
elif salary<=20000:
    print("Your HRA is", 0.25 * salary)
    print("Your DA is", 0.9 * salary)
    print("Gross Salary is ", salary + 0.25 * salary + 0.9 * salary)
else:
    print("Your HRA is", 0.3 * salary)
    print("Your DA is", 0.95 * salary)
    print("Gross Salary is ", salary + 0.3 * salary + 0.95 * salary)
