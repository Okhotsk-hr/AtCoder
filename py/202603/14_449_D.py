l,r,d,u= map(int,input().split())
count=0
for i in range(l,r+1):
    for j in range(d,u+1):
        if(max(abs(i),abs(j))%2==0):
            count+=1

print(count)