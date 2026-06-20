s=input()
ans=""
for i in range(len(s)):
    if(s[i].isdecimal()):
        ans+=s[i]
print(ans)