n,q=map(int,input().split())
a=list(map(int, input().split()))

for i in range(q):
    qu=list(map(int, input().split()))
    
    if(qu[0]==1):
        # a0=a[:qu[1]]
        # a1=a[qu[1]:]
        a=a[qu[1]:]+a[:qu[1]]
        #print(a)
    else:
        nums_sum=sum(a[qu[1]-1:qu[2]])
        print(nums_sum)
        # sum=0
        # for i in range(qu[1]-1,qu[2]):
        #     sum+=a[i]
        # print(sum)

