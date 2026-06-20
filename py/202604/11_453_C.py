n=int(input())
l=list(map(int, input().split()))
p=0.5
plus=True
num0=0
for i in range(len(l)):
    if(p>0):
        plus=True
        p-=l[i]
    else:
        plus=False
        p+=l[i]
    if(plus==(p<0)):
        num0+=1
    elif(plus==(p<0)):
        num0+=1

print(num0)