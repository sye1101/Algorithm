# N: 맵의 가로, 세로 크기
# S: 학생, T: 선생님, O: 장애물, X: 빈칸
import copy
from itertools import combinations
n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]
# 방향 정보
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
teachers = [(i, j) for  i in range(n) for j in range(n) if data[i][j] == 'T']
empty_spaces = [(i, j) for i in range(n) for j in range(n) if data[i][j] == 'X']
def watch(x, y, temp):
    for i in range(4):
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < n:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if temp[nx][ny] == 'O':
                    break # 감시 불가능
                if temp[nx][ny] == 'S':
                    return True # 감시 가능
    return False
def check(temp):
    for x, y in teachers:
        if watch(x, y, temp):
            return True
    return False
def simulate():
    for walls in combinations(empty_spaces, 3):
        temp = copy.deepcopy(data)
        for x, y in walls:
            temp[x][y] = 'O'
        if not check(temp):
            print('YES')
            return
    print('NO')
simulate()
"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
출력: YES
"""
"""
4
S S S T
X X X X
X X X X
T T T X
출력: NO
"""