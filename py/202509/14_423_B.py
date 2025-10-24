n=int(input())
l=list(map(int, input().split()))

room=[]
for i in range(n):
    room.append(0)

room.append(1)
room[0]=1

rpass=True
i=0
while(rpass):
    if(i<=n):
        if(l[i]==0):
            room[i+1]=1
        else:
            rpass=False
    else:
        rpass=False
    i+=1

rpass=True
i=n
while(rpass):
    if(i>0):
        if(l[i-1]==0):
            room[i-1]=1
        else:
            rpass=False
    else:
        rpass=False
    i-=1

count=0
for j in range(n+1):
    if(room[j]!=1):
        count+=1

print(count)



# l.append(1)

# count=0
# room=[]
# for i in range(n):
#     if(l[i]==1 and l[i+1]==1):
#         count+=1


# print(count)
