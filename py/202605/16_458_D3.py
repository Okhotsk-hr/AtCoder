#numpy.median関数

import numpy as np

x=int(input())
q=int(input())
nums=[x]

for i in range(q):
    ab=list(map(int, input().split()))
    nums+=ab
    print(int(np.median(nums)))
