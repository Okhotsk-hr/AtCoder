n=int(input())
a=list(map(int, input().split()))
a.sort()
print(a)

print(a[0]+a[n-1])