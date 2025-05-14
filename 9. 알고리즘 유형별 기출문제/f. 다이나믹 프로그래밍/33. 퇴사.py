n = int(input())
t = [] # 각 상담을 완료하는 데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # i일차부터 마지막 날까지 얻을 수 있는 최대 수익
max_value = 0 # 현재까지 최대 이익

for _ in range(n):
    x, y = map(int, input().split())
    t. append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i # # 상담이 끝나는 날
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value # 기존 최대값 유지

print(max_value)

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

출력: 45
"""

"""
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

출력: 55
"""

"""
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

출력: 20
"""

"""
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

출력: 90
"""