bill=0
print("WELCOME TO PIZZA POINT")
n=input("Enter the size of pizza, small,medium or large")
if n=='small' or n=='SMALL' or n=='Small':
	bill+=120
	print("Your bill is",bill)
if n=='medium' or n=='MEDIUM' or n=='Medium':
	bill+=170
	print("Your bill is",bill)
elif n=='large' or n=='LARGE' or n=='Large':
	bill+=350
	print("Your bill is",bill)
extra_cheese=input("Do you want extra cheese?")
if extra_cheese=='yes' or extra_cheese=='YES' or extra_cheese=='Yes':
	# bill+=70
	double=input("Want double cheese")
	single=input("Want single cheese")
	if single=='yes' or single=='YES' or single=="Yes":
		bill+=85
	elif double=='yes' or double=='YES' or double=='Yes':
		bill+=120
	print("Your bill is",bill)
else:
	print("your bill is ",bill)
# if extra_cheese=='n' or extra_cheese=='N':
# 	print("Your bill is",bill)
pepperoni=input("Do you want to add pepperoni ?")
if pepperoni=='yes' or pepperoni=='YES' or pepperoni=='Yes':
	bill+=65
	print("Your bill is",bill)
else:
	print("Your bill is",bill)
drink=input("Would you like to have softdrink ?")
if drink=='yes' or drink=='YES' or drink=='Yes':
	bill+=30
	print("Your bill is",bill)
else:
	print("Your bill is",bill)
ice_cream=input("Want Ice cream ?")
if ice_cream=='yes' or ice_cream=='YES' or ice_cream=='Yes':
	bill+=60
	print("your bill is",bill)
else:
	print("Your bill is ",bill)
print("Your Final Bill is",bill,"Rupees")
print("THANKS FOR VISITING PIZZA POINT")
print("Please Share your Feedback on our website, We will be highly delighted to you")
print("VISIT AGAIN\nFOR MORE INFORMATION VISIT OUR WEBSITE OR CALL ON- 1800 9800 7894")









