n=int(input())
xy= [[0 for j in range(2)] for i in range(n)]
for i in range(n):
    x,y=map(int,input().split())
    xy[i][0]=x
    xy[i][1]=y

count=0
for i in range(n):
    ok=True
    for j in range(n):
        if(i!=j):
            if(xy[j][0]<xy[i][0] and xy[j][1]<xy[i][1]):
                ok=False
    if(ok):
        count+=1

print(count)