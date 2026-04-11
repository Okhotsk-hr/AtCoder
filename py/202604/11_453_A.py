n=int(input());
s=input();

i=0;
while(s[i]=="o"and i<n-1):
    i+=1;

if(i!=n-1):
    print(s[i:]);
elif(i!=n and s[i]!="o"):
    print(s[-1]);
else:
    print("");