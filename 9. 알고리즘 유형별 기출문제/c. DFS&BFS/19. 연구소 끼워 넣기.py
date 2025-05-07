# N: 수의 개수
n = int(input())
# 숫자 리스트 생성
data = list(map(int, input().split()))
# 연산자 개수
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최소값과 최대값 업데이트
    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])
print(max_val)
print(min_val)

"""
2
5 6
0 0 1 0

출력: 30
30
"""

"""
3
3 4 5
1 0 1 0

출력: 35
17
"""

"""
6
1 2 3 4 5 6
2 1 1 1

출력: 54
-24
"""