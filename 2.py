a=int(input())
for i in range(0,a):
    b,d=map(int,input().split())
    r=b
    c=[int(x) for x in input().split()[:b]]
    for j in range (0,b):
        for k in range(j+1,b+1):
            e=c[j:k]
            w=len(e)
            if(sum(e)>=d):
                if(w<r):
                    r=w
                else:
                    continue
    print(r)  
