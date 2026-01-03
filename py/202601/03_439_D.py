n=int(input())
a = list(map(int, input().split()))
exe=[7,5,3]
count=0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            # print(str(i)+":"+str(j)+":"+str(k))
            nums=[a[i],a[j],a[k]]
            nums.sort(reverse=True)
            if(exe==nums):
                if(max(i,j,k)==j or min(i,j,k)==j):
                    count+=1
print(count)