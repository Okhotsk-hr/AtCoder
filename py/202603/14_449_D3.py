l,r,d,u= map(int,input().split())
count=0

for i in range(d,u+1):
    counta=0
    # counta=int(((abs(l)+abs(r))+1)/2)-abs(i)
    counta=int((abs(l)-abs(i)+1)/2)+int((abs(r)-abs(i)+1)/2)
    if(abs(i)%2==0):
        counta+=abs(i)*2
    print(counta)
    count+=counta

print(count)