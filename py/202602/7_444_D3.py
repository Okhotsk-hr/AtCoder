n=int(input())
a=list(map(int, input().split()))
b=0

for i in range(n):
    b0=["1" for j in range(a[i])]
    b+=int(''.join(b0))
print(b)