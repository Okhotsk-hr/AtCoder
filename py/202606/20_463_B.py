n,x=(map(str, input().split()))
ans=False
for i in range(int(n)):
    s=input()
    if(s[ord(x)-65]=="o"):
        ans=True

if(ans):
    print("Yes")
else:
    print("No")