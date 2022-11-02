def add(a):
    s=0
    n=a
    while True:
        s=0
        while n>0:
            r=n%10
            s+=r
            n=n//10
        if s<10:
            return s
        else:
            n=s
            s=0
            continue
a=int(input())
res=add(a)
print(res)