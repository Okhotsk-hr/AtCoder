n=int(input())
s=input()
a=[0]*n
for i in range(n):
    a[i]=i+1

for i in range(n):
    if(s[i]=="o"):
        #print(a[:i+1])
        aa=a[:i+1]
        aa.reverse()
        a=aa+a[i+1:]

ans=""
for i in range(n):
    ans+=str(a[i])+" "
print(ans)