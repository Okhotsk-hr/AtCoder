n=int(input())
ans= [[0] * n for i in range(n)]
r=0
c=int((n-1)/2)
k=1
ans[0][c]=1
while(k<=n*n-1):
    if(ans[int((r-1)%n)][int((c+1)%n)]==0):
        k+=1
        r=int((r-1)%n)
        c=int((c+1)%n)
        ans[r][c]=k
    else:
        k+=1
        r=int((r+1)%n)
        ans[r][c]=k

# for i in range(n):
#     for j in range(n):
#         if(i==0 and j==(n-1)/2):
#             ans[0][(n-1)/2]=1
            
#         else:
#             ans[i][j]=2
#         print(str(i)+":"+str(j))
# print(ans)

for i in range(n):
    pans=""
    for j in range(n):
        pans+=str(ans[i][j])+" "
    print(pans)