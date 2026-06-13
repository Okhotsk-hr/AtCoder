n,k,m=map(int,input().split())
stones=[[0] for i in range(n)]
for i in range(n):
    c,v=map(int,input().split())
    #stones[c][len(stones[c])]=v
    stones[c].append(v)

print(stones)
