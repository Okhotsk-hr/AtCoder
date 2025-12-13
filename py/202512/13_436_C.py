n,m= map(int,input().split())
squ= [[0] * n for i in range(n)]
count=0


for i in range(m):
    r,c=map(int,input().split())
    if(squ[r-1][c-1]==0 and squ[r][c-1]==0 and squ[r-1][c]==0 and squ[r][c]==0):
        squ[r-1][c-1]=1
        squ[r][c-1]=1
        squ[r-1][c]=1
        squ[r][c]=1
        count+=1

print(count)