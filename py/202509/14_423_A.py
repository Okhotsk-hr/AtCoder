x,c=map(int,input().split())
turn=True
i=1
while(turn):
    if((i*1000+i*c)>x):
        break
    else:
        i+=1

print(((i-1)*1000))