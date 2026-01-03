n=int(input())

count=0
nums=[]
turn=0
turnd=True

for i in range(n+1):
    turnd=True
    for y in range(2,i):
        if turnd:
            for x in range(1,y):
                turn+=1
                if x**2+y**2==i:
                    # print(str(x)+"+"+str(y))
                    count+=1
                    nums.append(i)
                    turnd=False


print(count)
ans=""
for i in range(len(nums)):
    ans+=str(nums[i])+" "
print(ans)
print(turn)