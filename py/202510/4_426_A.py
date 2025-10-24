x,y= map(str,input().split())
xn=0
yn=0

match x:
    case 'Ocelot':
        xn=1

    case 'Serval':
        xn=2

    case 'Lynx':
        xn=3

        
match y:
    case 'Ocelot':
        yn=1

    case 'Serval':
        yn=2

    case 'Lynx':
        yn=3

if(xn>=yn):
    print("Yes")
else:
    print("No")