n,m= map(int,input().split())
s=str(input())
t=str(input())
q=int(input())
takahashi=True
aoki=True
ans=[]

for i in range(q):
    w=str(input())
    takahashi=True
    aoki=True
    for j in range(len(w)):
        same=False
        for k in range(n):
            if(s[k]==w[j]):
                same=True
        if(same):
            takahashi=takahashi
        else:
            takahashi=False
        same=False
        for k in range(m):
            if(t[k]==w[j]):
                same=True
        if(same):
            aoki=aoki
        else:
            aoki=False

    if(takahashi and aoki):
        ans.append("Unknown")
    elif(takahashi):
        ans.append("Takahashi")
    elif(aoki):
        ans.append("Aoki")

for i in range(len(ans)):
    print(ans[i])

        
