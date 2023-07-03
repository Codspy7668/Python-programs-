a=[1,2,3,'list']
# p=a.split(a)
print(a)
print(a[2])
print(len(a))

s=input('Enter elements')
list=s.split()
print(list)

name=['ram','mohan','suresh','ramEsh']
print(name)
name[2]='naresh'
print(name)
print(name[3][3])


#1
l=list(map(int,input('enter space saperated integer=\n').split()))
a=i for i in l:
    if i%2==0:
        print(sum(a))

#2
s=input('enter a string=\n')
v=[i for i in s if i in 'aeiouAEIOU']
print(v)

#3
a=list(map(int,input('enter space seperated integers=\n').split()))
b=list(map(int,input('enter space seperated integers=\n').split()))
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

#4
c=0
n=int(input('enter a number=\n'))
for i in range(1,n+1):
    if n%i==0:
        c+=1
print('True') if c==2 else print('False')

#5
l=list(map(int,input('enter space saperated integer=\n').split()))
m=0
for i in l:
    m=i if i>m else m
print(m)

#6
s=input('enter a string=\n')
print("Yes") if s==s[::-1] else print("No")

#7
l=list(map(str,input('enter space seperated string=\n').split()))
print(max(l,key=len))

#8
n=input('enter your name=\n')
print(f'Hello nice to meat you Mr./Mrs.{n.title()}\nhope so your day\nwill be fine.')

#9
s=input('enter a string=\n')
l=s.split()
print(' '.join(l[::-1]))

#10
s=input('enter a string=\n')
l=s.split()
l=[l[i][::-1] for i in range(len(l)-1,-1,-1)]
print(' '.join(l))




n=int(input())
a=1
b=c=0
while c<n:
    c=a+b
    if c==n:
        c=-1
        break
    a=b
    b=c
print('yes') if c==-1 else print('no')

#2
n=input()
print(len(n.split()))

#3
n=input()
n=n.split()
r=0
for i in n:
    c=0
    for j in [*i]:
        if j in 'aeiouAEIOU':
            c+=1
        if c>1:
            r+=1
print(r)

#4
n=input()
n=[*n]
a=b=c=0
for i in n:
    if i in 'aeiou':
        a+=1
    if i in 'AEIOU':
        b+=1
    if i in '1234567890':
        c+=1
print('yes') if a!=0 and b!=0 and c!=0 else print('no')

#5
n=int(input())
l=[f'{n}*{i}={i*n}' for i in range(1,11)]
for i in l:
    print(i)

#6
a,b=map(int,input().split())
c=0
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        c=i
    i+=1
print(c)


#7
a,b=map(int,input().split())
c=0
for i in range(2,min(a,b)):
    if a%i==0 and b%i==0:
        c=1
        break
print(i) if c==1 else print(1)

#8
n=int(input())
c=[]
while n!=0:
    c.append(str(n%2))
    n//=2
print(''.join(c[::-1]))

#9
n=input()
print('yes') if '@gmail.com' in n and len(n)>10 else print('no')

#10
n=int(input())
e=n
p=len(str(n))
b=0
while n!=0:
    b+=(n%10)**p
    n//=10
print('yes') if b==e else print('no')