h,w=map(int,input().split())
ans=""
for i in range(h):
    for j in range(w):
        n=0
        if(h==1):
            n+=0
        elif(i==0):
            n+=1
        elif(i==h-1):
            n+=1
        else:
            n+=2
        if(w==1):
            n+=0
        elif(j==0):
            n+=1
        elif(j==w-1):
            n+=1
        else:
            n+=2
        ans+=str(n)+" "
    
    ans+="\n"

print(ans)
        
