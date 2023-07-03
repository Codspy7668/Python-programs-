import random
user=int(input('Enter your choice: 0 for rock, 1 for paper and 2 for scissors'))
computer=random.randint(0,2)
print("Computer choose:")
print(computer)
if computer==user:
    print("It's a draw")
elif computer > user:
    print("You Lose")
elif computer < user:
    print("You win")
elif computer==0 and user==2:
    print(" computer win")
elif computer==2 and user==0:
    print(" User win")
elif user<0:
    print("Enter valid input")
else:
    print("Enter the correct data type")
