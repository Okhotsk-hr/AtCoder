from collections import deque

# 100x100のグリッド内か判定
def in_field(x, y):
    return 1 <= x <= 100 and 1 <= y <= 100

# そのマスが安全か判定
def is_safe(x, y, A, B, C, D):
    return A <= x <= C and B <= y <= D

# 0-1 BFSでスタートからゴールまでの最小ダメージを計算
def min_damage(sx, sy, gx, gy, A, B, C, D):
    visited = [[-1] * 101 for _ in range(101)]
    dq = deque()
    dq.appendleft((sx, sy))
    visited[sx][sy] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if in_field(nx, ny) and visited[nx][ny] == -1:
                cost = 0 if is_safe(nx, ny, A, B, C, D) else 1
                visited[nx][ny] = visited[x][y] + cost
                if cost == 0:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))
    return visited[gx][gy]

def main():
    results = []
    while True:
        line = input()
        if line.strip() == "0":
            break
        N = int(line)
        A, B, C, D = map(int, input().split())
        waypoints = []
        for _ in range(N + 1):
            x, y = map(int, input().split())
            waypoints.append((x, y))
        
        total_damage = 0
        for i in range(N):
            sx, sy = waypoints[i]
            gx, gy = waypoints[i + 1]
            total_damage += min_damage(sx, sy, gx, gy, A, B, C, D)
        results.append(str(total_damage))

    print("\n".join(results))

if __name__ == "__main__":
    main()
