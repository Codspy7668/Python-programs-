unit=int(input("Enter the units consumed"))
if unit<=50:
    print("Your bill is ",0.50*unit)
    print("Total bill including charges is",0.50*unit+0.2*unit)
elif unit>50 and unit<=150:
    print("Your bill is",0.75*unit)
    print("Total bill including charges is", 0.75 * unit + 0.2 * unit)
elif unit>150 and unit<=250:
    print("Your bill is",1.20*unit)
    print("Total bill including charges is", 1.20 * unit + 0.2 * unit)
else:
    print("Your bill is",1.50*unit)
    print("Total bill including charges is", 1.50 * unit + 0.2 * unit)


