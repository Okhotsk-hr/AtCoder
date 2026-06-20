#statistics.median関数を使う
import statistics

x=int(input())
q=int(input())
nums=[x]

for i in range(q):
    ab=list(map(int, input().split()))
    nums+=ab
    print(statistics.median(nums))
