#D2→D11参考
n=int(input())
a=list(map(int, input().split()))
b=0

for i in range(len(a)):
    b0=(10**a[i]-1)//9
    b+=b0
print(b)