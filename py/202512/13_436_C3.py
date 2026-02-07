n,m= map(int,input().split())
on=[]
count=0


for i in range(m):
    r,c=map(int,input().split())
    r-=1
    c-=1
    if(((r*n+c) in on) or (((r+1)*n+c) in on) or ((r*n+c+1) in on) or (((r+1)*n+c+1) in on)):
        count=count
    else:
        on.append(r*n+c)
        on.append((r+1)*n+c)
        on.append(r*n+c+1)
        on.append((r+1)*n+c+1)
        count+=1
    # print(on)

print(count)