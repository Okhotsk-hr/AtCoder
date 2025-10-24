rt,ct,ra,ca = map(int,input().split())
n,m,l = map(int,input().split())
t=[rt,ct]
a=[ra,ca]

mt=[]
ms=[]


for i in range(m):
    m1,m2 = map(str,input().split())
    for j in range(int(m2)):
        mt.append(m1)

for i in range(l):
    l1,l2 = map(str,input().split())
    for j in range(int(l2)):
        ms.append(l1)

count=0
for i in range(n):
    match mt[i]:
        case 'U':
            t[0]-=1
        case 'D':
            t[0]+=1
        case 'R':
            t[1]+=1
        case 'L':
            t[1]-=1
    match ms[i]:
        case 'U':
            a[0]-=1
        case 'D':
            a[0]+=1
        case 'R':
            a[1]+=1
        case 'L':
            a[1]-=1
    if(t[0]==a[0]and t[1]==t[1]):
        count+=1

print(count)
