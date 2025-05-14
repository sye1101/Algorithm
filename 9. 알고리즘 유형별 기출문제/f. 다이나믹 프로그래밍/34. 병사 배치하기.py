n = int(input())
array = list(map(int, input().split()))
array.reverse() # 전투력을 '오름차순 LIS'로 바꾸기 위해 뒤집음

dp = [1] * n # dp[i]: i번째 원소까지 봤을 때 LIS의 최대 길이

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))