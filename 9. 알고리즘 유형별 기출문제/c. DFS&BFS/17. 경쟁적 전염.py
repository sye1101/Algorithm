# N: 시험관의 가로, 세로 크기
# K: 바이러스 종류 수
# 구해야 하는 것: S초 뒤에 (X, Y)에 존재하는 바이러스 종류. 존재 x -> 0 출력
from collections import deque

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

target_s, target_x, target_y = map(int, input().split())

# 방향 정보
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus = []
for i in range(n):
    for j in range(n):
        if not data[i][j] == 0:
            virus.append((data[i][j], 0, i, j))
# 바이러스 번호 순 정렬
virus.sort()
q = deque(virus)

# bfs
while q:
    virus_type, sec, x, y = q.popleft()
    if sec == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = virus_type
            q.append((data[nx][ny], sec + 1, nx, ny))

# 문제는 1행 1열부터 존재. data는 0행 0열부터 존재, -> x, y 위치 -1씩 하기
print(data[target_x-1][target_y-1])

"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2

출력: 3
"""

"""
3 3
1 0 2
0 0 0
3 0 0
1 2 2

출력: 0
"""