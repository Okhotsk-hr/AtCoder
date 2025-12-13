n=int(input())
s=input()

ans=""
for i in range(n-len(s)):
    ans+="o"
ans+=s
print(ans)