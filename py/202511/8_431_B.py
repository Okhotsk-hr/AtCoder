x=int(input())
n=int(input())
w = list(map(int, input().split()))
q=int(input())
plist=[]
for i in range(n):
    plist.append(0)
for i in range(q):
    p=int(input())
    if(plist[p-1]==0):
        x+=w[p-1]
        plist[p-1]=1
    else:
        x-=w[p-1]
        plist[p-1]=0
    print(x)
