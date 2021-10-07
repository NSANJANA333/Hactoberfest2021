a=int(input())
b=str(a)
k=0
c=b[::-1]
if (b==c):
    for i in range(2,a+1):
        if(a%i==0):
            k=k+1
    if(k==1):
        print("Yes")
    else:
        print("No")   
else:
    print("No")
