# N: 땅의 크기
# L명 이상, R명 이하
from collections import deque

n ,l ,r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, idx):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = idx # 현재 연합의 번호 할당
    summary = data[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = idx
                    summary += data[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        data[i][j] = summary // count
    return count

total_cnt = 0
# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)] # 각 나라가 어느 연합에 속했는지
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리 x
                bfs(i, j, idx)
                idx += 1
    if idx == n * n: # 모든 나라가 연합을 이루지 못한 경우 -> 종료
        break
    total_cnt += 1

print(total_cnt)