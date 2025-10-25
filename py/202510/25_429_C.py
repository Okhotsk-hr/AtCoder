n=int(input())
a = list(map(int, input().split()))

count=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            # print(str(i+1)+","+str(j+1)+","+str(k+1))
            if(a[i]==a[j] and a[i]!=a[k]):
                count+=1
            elif(a[j]==a[k] and a[j]!=a[i]):
                count+=1
            elif(a[k]==a[i] and a[k]!=a[j]):
                count+=1
            
print(count)

