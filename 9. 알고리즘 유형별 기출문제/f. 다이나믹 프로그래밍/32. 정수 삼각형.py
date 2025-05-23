# n: 삼각형의 크기
# 대각선 왼쪽 혹은 대각선 오른쪽 선택 가능
n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

    for i in range(1, n):
        for j in range(i + 1):
            # 왼쪽 위에서 내려오는 경우
            if  j == 0:
                up_left = 0
            else:
                up_left = dp[i - 1][j - 1]
            # 바로 위에서 내려오는 경우
            if j == i:
                up = 0
            else:
                up = dp[i - 1][j]
            # 최대 합을 저장
            dp[i][j] = dp[i][j] + max(up_left, up)

    print(max(dp[n - 1]))