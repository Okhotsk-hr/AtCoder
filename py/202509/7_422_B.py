h,w=map(int,input().split())
s = [input() for _ in range(h)]
rule=True

for i in range(h):
    for j in range(w):
        if(s[i][j]=='#'):
            count=0
            if(i>0):
                if(s[i-1][j]=='#'):
                    count+=1
            if(i<h-1):
                if(s[i+1][j]=='#'):
                    count+=1
            if(j>0):
                if(s[i][j-1]=='#'):
                    count+=1
            if(j<w-1):
                if(s[i][j+1]=='#'):
                    count+=1
            if(count!=2 and count!=4):
                rule=False
                break

if(rule):
    print("Yes")
else:
    print("No")
