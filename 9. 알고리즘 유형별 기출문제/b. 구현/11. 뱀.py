# N: 보드의 크기
# K: 사과의 개수
# L: 뱀의 방향 변환 횟수
# X: 방향 변환 시간 정보
# C: 변환할 방향 정보
n = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

# 사과 정보 입력
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방향 회전 정보 입력
l = int(input())
change_directions = []
for _ in range(l):
    x, c = input().split()
    change_directions.append((int(x), c))

def turn(direction, c):
    if c == 'L':  # 왼쪽
        direction = (direction - 1) % 4
    else:  # 오른쪽
        direction = (direction + 1) % 4
    return  direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치
    sec = 0
    idx = 0
    direction = 1
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dr[direction]
        ny = y + dc[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과가 없는 경우
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            # 사과가 있는 경우
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else: # 벽이나 뱀의 몸통과 부딪히는 경우
            sec += 1
            break
        x, y = nx, ny # 다음 위치로 머리 이동
        sec += 1
        if idx < l and sec == change_directions[idx][0]:
            direction = turn(direction, change_directions[idx][1])
            idx += 1
    return sec

print(simulate())

"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

출력: 9
"""

"""
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

출력: 21
"""