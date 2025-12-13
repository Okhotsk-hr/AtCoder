n,m= map(int,input().split())
on=[]
count=0


for i in range(m):
    r,c=map(int,input().split())
    if(not((r*n+c) in on)):
        on.append(r*n+c)
        on.append((r-1)*n+c)
        on.append((r+1)*n+c)
        on.append(r*n+c-1)
        on.append((r-1)*n+c-1)
        on.append((r+1)*n+c-1)
        on.append(r*n+c+1)
        on.append((r-1)*n+c+1)
        on.append((r+1)*n+c+1)
        count+=1

print(count)