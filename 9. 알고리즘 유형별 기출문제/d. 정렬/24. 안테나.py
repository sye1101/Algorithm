# N: 집의 수
n = int(input())
data = list(map(int, input().split()))

data.sort()

print(data[(n-1)//2])