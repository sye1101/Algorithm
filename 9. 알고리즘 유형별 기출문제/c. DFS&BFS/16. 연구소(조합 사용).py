import copy
from itertools import combinations
# N: 지도의 세로 크기
# M: 지도의 가로 크기
# 0: 빈칸, 1: 벽, 2: 바이러스
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스 전파
def spread_virus(temp):
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                dfs(temp, i, j)

def dfs(temp, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            dfs(temp, nx, ny)

def get_safe_area(temp):
    return sum(row.count(0) for row in temp)

# 빈칸인 위치 리스트에 저장
empty_spaces = [(i, j) for i in range(n) for j in range(m) if data[i][j] == 0]

# 조합 사용하여 빈칸 중 3개 벽 세우기
for walls in combinations(empty_spaces, 3):
    temp = copy.deepcopy(data)
    for x, y in walls:
        temp[x][y] = 1
    spread_virus(temp)
    result = max(result, get_safe_area(temp))

print(result)

"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

출력: 27
"""

"""
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

출력: 9
"""