#逃げ恥貴族
N,Q=(map(int,input().split()))
A=[1 for x in range(N+1)]
A[0]=0
saitei=0
ans=[]

for i in range(Q):
    X,Y=(map(int,input().split()))
    a=sum(A[saitei:X+1])
    ans.append(a)
    A[Y]+=a
    #print(A[saitei:X+1])
    saitei=max(saitei,X+1)
    #print(saitei)
    #print(A)

for i in range(len(ans)):
    print(ans[i])