n=int(input())
a=list(map(int, input().split()))
b=0
b0=[]

for i in range(n):
    for j in range(a[i]):
        if(len(b0)<=j):
            b0.append(1)
        else:
            b0[j]+=1

for i in range(len(b0)):
    b+=b0[i]*(10**i)

print(b)