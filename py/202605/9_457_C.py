n,k=map(int,input().split())
a = [list(map(int, input().split())) for l in range(n)]
c=list(map(int, input().split()))
b=[]
numb=0
for i in range(n):
    # b+=(a[i][1:])*c[i]
    numb+=len(a[i][1:])*c[i]
    if numb>=k:
        if len(a[i][1:])>1:
            print(a[i][(k-numb+len(a[i][1:])*c[i])%len(a[i][1:])])
        else:
            print(a[i][1])
            #print((k-numb+len(a[i][1:])*c[i])%len(a[i][1:]))
        break


# # print(b)
# print(b[k-1])