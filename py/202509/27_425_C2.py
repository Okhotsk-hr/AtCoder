N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (2 * N + 1)
for i in range(2 * N):
    B[i + 1] = B[i] + A[i % N]

pos = 0
for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        pos = (pos + query[1]) % N
    else:
        l, r = query[1] - 1, query[2]
        l += pos
        r += pos
        ans = B[r] - B[l]
        print(ans)