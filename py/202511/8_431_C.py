import sys

n,m,k= map(int,input().split())
h = list(map(int, input().split()))
b = list(map(int, input().split()))

h.sort()
b.sort()

print(h)
print(b)
l=0

for i in range(k):
    j=l
    search=True
    while search:
        if(j>=m):
            print("No")
            sys.exit()
        if(h[i]<=b[j]):
            search=False
            l=j+1
        print(str(h[i])+":"+str(b[j]))
        j+=1

print("Yes")