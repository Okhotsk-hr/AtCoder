n=int(input())
h=[0]*n
l=[0]*n
for i in range(n):
    h[i],l[i]=(map(int, input().split()))
    
# print(h)
# print(l)

q=int(input())
t=list(map(int,input().split()))

# print(t)

for i in range(q):
    line=0
    while(l[line]<=t[i]):
        line+=1
    print(max(h[line:]))