s=input()
str1=0
str2=0
s2=None
ans=True

for i in range(len(s)):
    if(s[i]==s[0]):
        str1+=1
    elif(s2==None):
        s2=s[i]
        str2+=1
    elif(s[i]==s2):
        str2+=1

if(str1==1):
    print(s[0])
else:
    print(s2)