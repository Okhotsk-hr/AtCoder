t=int(input())
for i in range(t):
    eggs=[]
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in range(n):
        eggs.append(a[j])
        k=0
        while b[j]>0:
            if(eggs[k]>b[j]):
                eggs[k]-=b[j]
                b[j]=0
            elif(eggs[k]==b[j]):
                eggs[k]=0
                b[j]=0
            else:
                b[j]-=eggs[k]
                eggs[k]=0
            k+=1
        if(j-d>=0):
            eggs[j-d]=0
    print(sum(eggs))