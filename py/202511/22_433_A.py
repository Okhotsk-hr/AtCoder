import sys

x,y,z= map(int,input().split())

while (x<=500 and y<=500):
    print("do")
    if(x==y*z):
        print("Yes")
        sys.exit()#条件を満たしたのでプログラム終了
    x+=1
    y+=1

print("No")