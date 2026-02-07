
n=int(input())
a=list(map(int, input().split()))
b0=[]
b=[]

for i in range(len(a)):
    b0=[]
    for k in range(a[i]):
        b0.append("1")
    b.append(int(''.join(b0)))
print(sum(b))
