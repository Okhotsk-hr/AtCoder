t=int(input())

for i in range(t):
    # print("reset")
    a=input()
    b=input()
    j=0
    while(j<min(len(a),len(b))):
        # print(j)
        if(a[j]!=b[j]):
            # print("不一致")
            # print(a[j:j+2])
            if(a[j:j+2]=="xx"):
                # print(a[j:j+2])
                # print("↓")
                # print(a[:j]+"(xx)"+a[j+2:])
                a=str(a[:j]+"(xx)"+a[j+2:])
                j-=1
            elif(a[j:j+4]=="(xx)"):
                # print(a[j:j+4])
                # print("↓")
                # print(a[:j]+"xx"+a[j+4:])
                a=str(a[:j]+"xx"+a[j+4:])
                j-=1
        j+=1
    print("結果")
    print(a)
    print(b)
    print(a==b)