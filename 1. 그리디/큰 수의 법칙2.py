# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K: 연속해서 초과 불가능한 횟수
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
# K+1: 반복되는 수열의 길이. 가장 큰 수 K개와 두 번째로 큰 수 1개
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)