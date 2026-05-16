x=int(input())
q=int(input())
nums=[x]
np=0

for i in range(q):
    ab=list(map(int, input().split()))
    nums+=ab
    np+=1
    nums.sort()
    print(nums[np])
