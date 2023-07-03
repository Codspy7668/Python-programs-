import random
# Using random choice
# list=['jenny', 'jiya' ,'rohan' ,'rahul']
# a=random.choice(list)
# print(a)
# print(a,'will pay the bill')

# text='welcome to the world'
# split=text.split(' ')
# print(split)
#withour choice

a=input('Enter name')
list=a.split(' ')
# print(list)
c=random.randint(0,len(list)-1)
print(f"{list[c]} will pay the bill")

