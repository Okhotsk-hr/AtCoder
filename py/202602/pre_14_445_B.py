n=int(input())
s=[]
ans=[]
max=0
for i in range(n):
    s.append(str(input()))
    if(len(s[i])>max):
        max=len(s[i])

for i in range(n):
    ans.append("")
    num=max-len(s[i])
    for j in range(num//2):
        ans[i]=ans[i]+"."
    ans[i]=ans[i]+s[i]
    for j in range(num//2):
        ans[i]=ans[i]+"."


print('\n'.join(ans))
