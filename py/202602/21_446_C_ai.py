t=int(input())
for i in range(t):
    eggs=[]
    n,d=map(int,input().split())
    eggs=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in range(n):
        k = max(0, j - d)
        eggs[k] -= b[j]
        if eggs[k] < 0:
            if k + 1 < n:
                eggs[k + 1] += eggs[k]
            eggs[k] = 0
        if j - d >= 0:
            eggs[j - d] = 0
    print(sum(eggs))