x=int(input())
q=int(input())
nums=[x]
np=0

for i in range(q):
    a,b=map(int, input().split())
    turn=True
    j=0
    while(turn and j<len(nums)):
        if(nums[j]>=a):
            # subnums=nums
            # nums=subnums[:j+1]  
            # nums[j]=a
            # nums+=subnums[j:]
            nums.insert(j,a)
            turn=False
        j+=1
    if(turn):
        nums.append(a)


    turn=True
    j=0
    while(turn and j<len(nums)):
        if(nums[j]>=b):
            # subnums=nums
            # nums=subnums[:j+1]  
            # nums[j]=b
            # nums+=subnums[j:]
            nums.insert(j,b)
            turn=False
        j+=1
    if(turn):
        nums.append(b)


    np+=1
    print(nums[np])


    
    # np+=1
    # nums.sort()
    #print(nums[np])
