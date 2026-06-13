n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

correct=True
for i in range(n):
    if(b[a[i]-1]-1!=i):
        correct=False
        break

if(correct):
    print("Yes")
else:
    print("No")