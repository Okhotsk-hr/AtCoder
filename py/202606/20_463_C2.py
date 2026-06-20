import sys
from bisect import bisect_right

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
h = [0] * n
l = [0] * n
for i in range(n):
    h[i] = next(it)
    l[i] = next(it)

q = next(it)
t = [next(it) for _ in range(q)]

suf = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suf[i] = max(suf[i + 1], h[i])

out = []
for x in t:
    out.append(str(suf[bisect_right(l, x)]))

sys.stdout.write("\n".join(out))