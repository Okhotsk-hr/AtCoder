n=str(input())
num=n

for j in range(1000):
    n=str(num)
    num=0
    for i in range(len(n)):
        num+=int(n[i])**2
    if num==1:
        print("Yes")
        exit()

print("No")
