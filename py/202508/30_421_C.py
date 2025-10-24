n=int(input())*2
s0=input()

count=0
s=[]
for i in range(n):
    s.append(s0[i])

# k=n-2
tf=True

while tf:
    for i in range(n-2):
        if(s[i]==s[i+1]and s[i+1]!=s[i+2]):
            a=s[i+2]
            s[i+2]=s[i+1]
            s[i+1]=a
            count+=1
            #k-=1

            ans=""
            for i in range(n):
                ans+=s[i]
            print(ans)
        
    tf=False
    for i in range(n-1):
        if(s[i]==s[i+1]):
            tf=True

ans=""
for i in range(n):
    ans+=s[i]

#print(ans)
print(count)




