
n,m = map(int,input().split())
s=[]
h=[0 for i in range(n)]
for i in range(n):
    s.append(input())
#print(s)

num=[0,0]

for i in range(m):
    num=[0,0]
    n0=[]
    n1=[]
    for j in range(n):
        num[int(s[j][i])]+=1
        #print(int(s[j][i]))
    #print(num)
    # if(num[0]>num[1]):
    #     for j in range(n):
    #         if(s[j][i]=='1'):
    #             h[j]+=1
    for j in range(n):
        if(num[0]==0 or num[1]==0):
            h[j]+=1
        elif(s[j][i]=='1' and num[0]>num[1]):
            h[j]+=1
        elif(s[j][i]=='0' and num[0]<num[1]):
            h[j]+=1

#print(h)
h2=sorted(h, reverse=True)
# print(h2)
ans=''
for i in range(n):
    if(h[i]==h2[0]):
        ans+=str(i+1)+' '
        #print(i+1)

print(ans)