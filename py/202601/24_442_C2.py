n,m= map(int,input().split())
ans=""
members=[[True for b in range(n)] for a in range(n)]

# ここをcount=-1で置き換え
# for i in range(n):
#     members[i][i]=False

for i in range(m):
    a,b= map(int,input().split())
    a-=1
    b-=1
    members[a][b]=False
    members[b][a]=False

for i in range(n):
    count=-1
    for j in range(n):
        if(members[i][j]):
            count+=1
    if(count<=2):
        ans+="0"
    else:
        ans+=str(int((count*(count-1)*(count-2))/6))
    ans+=" "

print(ans)