s=input()
ans=0
for i in range(len(s)):
    if(s[i]=="C"):
        ans+=min(i+1,len(s)-i)
print(ans)