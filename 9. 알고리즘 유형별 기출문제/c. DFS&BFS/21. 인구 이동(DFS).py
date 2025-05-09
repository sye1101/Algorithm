n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, idx):
    union[x][y] = idx
    united.append((x, y))
    global summary, count
    summary += data[x][y]
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
            if l <= abs(data[nx][ny] - data[x][y]) <= r:
                dfs(nx, ny, idx)

total_cnt = 0
while True:
    union = [[-1] * n for _ in range(n)]
    idx = 0
    changed = False

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                united = []
                summary = 0
                count = 0
                dfs(i, j, idx)
                if count > 1:
                    changed = True
                    for x, y in united:
                        data[x][y] = summary // count
                idx += 1

    if not changed:
        break
    total_cnt += 1

print(total_cnt)