n,q = map(int,input().split())
a0 = list(map(int, input().split()))
b0 = list(map(int, input().split()))

def sigma(k):
    if(k==0):
        return min(a[k],b[k])  
    else:
        return min(a[k],b[k])+sigma(k-1)
    
for i in range(q):
    c = list(map(str, input().split()))
    a=a0
    b=b0
    sum=0
    if(c[0]=='A'):
        #print('A')
        a[int(c[1])-1]=int(c[2])
    elif(c[0]=='B'):
        #print('B')
        b[int(c[1])-1]=int(c[2])
    # print(a)
    # print(b)
    # for k in range(n):
    #     #print(str(a[k])+"/"+str(b[k]))
    #     sum+=min(a[k],b[k])
    
    print(sigma(n-1))



