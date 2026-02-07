n=int(input())
a=list(map(int, input().split()))
b0=0
b=0

for i in range(len(a)):
    b0=0
    for k in range(a[i]):
        b0=b0*10+1
    b+=b0
print(b)