t=int(input())
c=0
for i in range (t):
    a=input()
    b=len(a)
    if (a==a[::-1]):
        c=c+b
print(c)
