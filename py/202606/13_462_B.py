n=int(input())
g= [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    a=list(map(int,input().split()))
    # print("turn"+str(i))
    for j in range(1,a[0]+1):
        g[a[j]-1][i]=i+1

# print(g)
ans=""
for i in range(n):
    count=0
    line=""
    # print(g[i])
    for j in range(len(g[i])):
        if(g[i][j]!=0):
            count+=1
            line+=" "+str(g[i][j])
    ans+=str(count)+line+"\n"

print(ans)
