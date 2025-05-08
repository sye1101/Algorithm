# N: 맵의 가로, 세로 크기
# S: 학생, T: 선생님, O: 장애물, X: 빈칸
import copy
from itertools import combinations

n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]

# 방향 정보
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(temp):
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 'S':
                dfs(i, j)

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and data[nx][ny] != 'O':
            if data[nx][ny] == 'S':
                return True # 감시 가능
            else:
                nx += dx[i]
                ny += dy[i]
    return False

empty_spaces = [(i, j) for i in range(n) for j in range(n) if data[i][j] == 'X']

flag = False
def simulate():
    for walls in combinations(empty_spaces, 3):
        temp = copy.deepcopy(data)
        for x, y in walls:
            temp[x][y] = 'O'
        check(temp)
        if flag:
            print('YES')
            return

    print('NO')

simulate()