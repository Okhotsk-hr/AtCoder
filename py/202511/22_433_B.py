
n=int(input())
a = list(map(int, input().split()))

search=True
for i in range(len(a)):
    search=True
    for j in range(1,i+1):
        if(i==0):
            print(-1)
        if(search):
            if(a[i]<a[i-j]):
                print(i-j+1)
                search=False
    if(search):
        print(-1)
