n,q = map(int,input().split())
a0 = list(map(int, input().split()))
b0 = list(map(int, input().split()))

# def sigma(k,n,a,b):
#     if(k-1==n):
#         return min(a[k],b[k])
#     else:
#         return min(a[k],b[k])+sigma(k+1,n,a,b)
    
c = [[str(x) for x in input().split()] for i in range(q)]
#print(c)
# print(c[q-1][0])

for i in range(q):
    #c = list(map(str, input().split()))
    a=a0
    b=b0
    sum=0
    if(c[i][0]=='A'):
        #print('A')
        a[int(c[i][1])-1]=int(c[i][2])
    elif(c[i][0]=='B'):
        #print('B')
        b[int(c[i][1])-1]=int(c[i][2])
    # print(a)
    # print(b)
    for k in range(n):
        #print(str(a[k])+"/"+str(b[k]))
        sum+=min(a[k],b[k])
        
    #sigma(0,n,a,b)
    print(sum)



