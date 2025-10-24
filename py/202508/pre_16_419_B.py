q=input()
list=[]

for i in range(int(q)):
    que=input()
    if(que[0]=='1'):
        t,x = map(int,que.split())
        list.append(x)
    elif(que[0]=='2'):
        list.sort()
        print(list.pop(0))
