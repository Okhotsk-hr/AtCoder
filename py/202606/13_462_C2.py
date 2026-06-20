import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))
pts = [(int(next(it)), int(next(it))) for _ in range(n)]

pts.sort()
INF = 10**30
min_y = INF
count = 0
i = 0
while i < n:
    j = i
    # group points with the same x
    while j < n and pts[j][0] == pts[i][0]:
        j += 1
    # collect ys for the group
    group_ys = [pts[k][1] for k in range(i, j)]
    # a point is good if no previous point has y < its y
    for y in group_ys:
        if y <= min_y:
            count += 1
    # update min_y with the smallest y in this group
    min_y = min(min_y, min(group_ys))
    i = j

sys.stdout.write(str(count))