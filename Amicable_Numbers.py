a=int(input())
b=int(input())
i=1
j=1
s=0
m=0
for i in range(1,a):
    if (a%i==0):
        s+=i
        i+=1
for j in range(1,b):
    if(b%j==0):
        m+=j
        j+=1
if (s==b) and (m==a):
    print('Amicable')
else:
    print('Not Amicable')
    