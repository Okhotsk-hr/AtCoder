n=int(input())
a=list(map(int, input().split()))
b=0
b0=[0]*max(a)

for i in range(n):
    for j in range(a[i]):
        b0[j]+=1

for i in range(len(b0)):
    b+=b0[i]*(10**i)

print(b)