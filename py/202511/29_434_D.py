sky=[[0]*2000]*2000
n=int(input())
num=4
cloud=[input().split() for num in range(n)]
print(cloud)
count_sky=2000*2000

for k in range(n):
    sky=[[0]*2000]*2000
    count_sky=2000*2000
    for i in range(n):
        if(i!=k):
            for j in range(int(cloud[i][0])-1,int(cloud[i][1])):
                for l in range(int(cloud[i][2])-1,int(cloud[i][3])):
                    print(cloud[i][0]+"/"+cloud[i][1]+"/"+cloud[i][2]+"/"+cloud[i][3])
                    print(str(j)+"/"+str(l))
                    if(sky[j][l]!=1):
                        print("雲")
                        sky[j][l]=1
                        count_sky-=1
    print(count_sky)