t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()[:n]]
    a=sorted(a)
    for i in range (0,n):
        c=0
        for j in range (0,n):
            if(a[i]==a[j]):
                c=c+1
    if(c==1):
        print(a[i])
