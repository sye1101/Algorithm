# N: 집의 개수
# C: 공유기의 개수
n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

start = 1 # 가능한 최소 거리
end = home[-1] - home[0] # 가능한 최대 거리
result = 0

while (start <= end):
    mid = (start + end) // 2 # 현재 공유기 간 최소 거리 후보
    value = home[0] # 처음 집에 공유기 설치
    count = 1
    for i in range(1, n):
        if home[i] >= value + mid: # 최소 거리 만족 -> 공유기 설치 가능
            value = home[i]
            count += 1
    if count >= c: # 공유기 설치 완료 -> 최소 거리 증가
        start = mid + 1
        result = mid
    else: # 공유기 설치 불가 -> 최소 거리 감소
        end = mid - 1

print(result)

"""
5 3
1
2
8
4
9

출력: 3
"""