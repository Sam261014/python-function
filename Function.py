def prime(x):
    p=0
    for i in range(2,x//2+1):
        if x%i==0:
            p=1
    return p

n=int(input("Enter no "))
x=prime(n)
if  x==0:
    print("Its prime no")
else:
    print("Not Prime")
