n = int(input())
a = list(map(int, input().split()))
b = sum((10**x - 1) // 9 for x in a)
print(b)