n=int(input())
a = list(map(int, input().split()))
i=0
c=True
while(c):
    #print(i)
    if(i>=n):
        i=n
        break
    if(a[i]-1!=0):
        i+=a[i]-1
    else:
        i+=1
        c=False
        
print(i)