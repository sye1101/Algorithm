# N: 모험가 수
n = int(input())

# N명의 공포도 배열
array = list(map(int, input().split()))
# 공포도 오름차순
array.sort()

# result: 총 그룹의 수
result = 0
# count: 현재 그룹의 모험가의 수
count = 0

for i in array:
    count += 1
    if count >= i: # 현재의 공포도 이상이라면, 그룹 결성
        result += 1
        count = 0

print(result)

"""
5
2 3 1 2 2

출력: 2
"""