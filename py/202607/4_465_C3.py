n=int(input())
s=input()

a=[i for i in range(1,n+1)]

for i in range(n):
    if(s[i]=="o"):
        a=[a[:i+1][i] for i in range(len(a[:i+1]) - 1, -1, -1)]+a[i+1:]

print(*a)# 内包表記でやってみる?
