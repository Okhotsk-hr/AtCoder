n,k=map(int,input().split())
a=list(map(int, input().split()))

nums=[0]*(max(a)+1)
max=max(a)
sum=[]
for i in range(max):
    nums[a[i]]+=a[i]

for i in range(max):
    numx=nums[i]
    nums[i]=0
    sum[i]=sum(nums)
    nums[i]=numx

print(min(sum))

              