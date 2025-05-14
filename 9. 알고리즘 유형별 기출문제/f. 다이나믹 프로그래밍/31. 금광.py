T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    dp = []
    idx = 0
    for i in range(n):
        dp.append(data[idx:idx + m])
        idx += m

    for j in range(1, m): # 열로 이동
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0 # 맨 위면 위쪽에서 못 옴
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0 # 맨 아래면 아래쪽에서 못 옴
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력: 19
16
"""