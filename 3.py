t=int(input())
c=[]
l=0
m=0
x=0
for i in range (0,t):
    b=[int(x) for x in input().split()[0:t]]
    c.append(b)
for j in range (0,t):
    l=l+c[j][j]
    m=m+c[j][t-j-1]
print(abs(l-m))
