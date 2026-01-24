q=int(input())
sound=0
playing=False
for i in range(q):
    a=int(input())
    if a==1:
        sound+=1
    elif a==2:
        if sound>=1:
            sound-=1
    elif a==3:
        if playing:
            playing=False
        else:
            playing=True
    if(sound>=3 and playing):
        print("Yes")
    else:
        print("No")