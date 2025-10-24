n=int(input())
a=list(map(int, input().split()))
count=[]
ans=[]
num=[]
output=""
do=True
for i in range(n):
    count.append(0)
    ans.append(0)
    num.append(i+1)
count.append(0)

for i in range(n):
    if(a[i]!=-1):
        count[a[i]]+=1
        if(count[a[i]]>=2):
            do=False
        
if(do):
    print("Yes")
    for i in range(n):
        if(a[i]!=-1):
            ans[i]=a[i]
            num[a[i]-1]=0
            # print(ans)
            # print(num)
            # print("a")

    j=0
    for i in range(n):
        if(ans[i]==0):
            while(num[j]==0):
                j+=1
            ans[i]=num[j]
            j+=1
            # if(num[j]!=0):
            #     ans[i]=num[j]
            #     j+=1
            # else:
            #     j+=1
            #     ans[i]=num[j]
            #     j+=1
            # print(ans)
            # print(num)
            # print("b")

    for i in range(len(ans)):
        output+=str(ans[i])+" "

    print(output)
else:
    print("No")



