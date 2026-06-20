points=[1]
for i in range(1,10*6+1):
    if(i%2==0):
        points.append(i*2*4)
    else:
        points.append(0)

l,r,d,u= map(int,input().split())
count=0

