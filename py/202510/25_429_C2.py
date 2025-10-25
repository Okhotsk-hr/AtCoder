import math

n=int(input())
a = list(map(int, input().split()))
count=[]
for i in range(n):
    count.append(0)

for i in range(n):
    count[a[i]-1]+=1
# print(count)

countk=1
countp=0
knum=[]

for i in range(n):
    if(count[i]==1):
        countp+=1
    elif(count[i]>=2):
        countk*=count[i]
        knum.append(count[i])

count2=0
if(len(knum)>=2):
    for i in range(len(knum)):
        knum2=knum[:i]+knum[i+1:]
        for j in range(len(knum2)):
            knum2[j]-=1
        count2+=knum[i]*(math.prod(knum2))


ans=countp*countk
if(countk==1):
    ans=0

print(count2+ans)