h,w=map(int,input().split())
s=[[""]*w]*h
for i in range(h):
    ins=input()
    print(ins)
    for j in range(w):
        if(ins[j]=="."):
            s[i][j]="."
        else:
            s[i][j]="#"

# s = [input() for _ in range(h)]
print(s)