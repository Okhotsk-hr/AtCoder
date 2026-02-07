n=int(input())
a = list(map(int, input().split()))
exe=[7,5,3]
count=0

for i in range(n):
    if(a[i]%7==0):
        for j in range(n):
            if(a[j]%5==0):
                for k in range(n):
                    if(a[k]%3==0 and a[i]/7==a[j]/5 and a[i]/7==a[k]/3):
                        if(max(i,j,k)==j or min(i,j,k)==j):
                            #print(str(i)+":"+str(j)+":"+str(k))
                            count+=1


print(count)