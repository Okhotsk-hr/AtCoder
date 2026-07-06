# abが完全にxyの外だった場合にマイナスになる
x,y,l,r,a,b=map(int,input().split())
sum=0
sumt=b-a
if(l-a>=0):
  sum+=(l-a)*y
  sumt-=(l-a)
if(b-r>=0):
  sum+=(b-r)*y
  sumt-=(b-r)
sum+=sumt*x

print(sum)