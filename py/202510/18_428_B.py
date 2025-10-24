n,k= map(int,input().split())
s=str(input())

# i=n-k+1
# t=s[i-1:i+k-1]
# print(t)
t=[[],[]]

t[0].append(s[0:k])
t[1].append(1)
max=1
#print(t[1][0])
for i in range(1,n-k+1):
    sea=True
    for j in range(len(t[0])-1):
        if(t[0][j]==s[i:i+k]):
            t[1][j]+=1
            sea=False
            if(t[1][j]>max):
                max=t[1][j]
    if(sea):
        t[0].append(s[i:i+k])
        t[1].append(1)
    
print(max)
#print(t)
ans=[]

for i in range(len(t[0])):
    if(t[1][i]==max):
        ans.append(t[0][i])
# print(ans)
ans.sort()
ansp=""

for i in range(len(ans)):
    ansp+=ans[i]+" "
print(ansp)
