n=int(input())
a=list(map(int, input().split()))

b=[int(''.join(["1" for j in range(a[i])])) for i in range(n)]
print(sum(b))
