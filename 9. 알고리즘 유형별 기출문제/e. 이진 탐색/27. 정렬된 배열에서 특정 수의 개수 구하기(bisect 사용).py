import bisect

def count_x(array, left_value, right_value):
    right_idx = bisect.bisect_right(array, right_value)
    left_idx = bisect.bisect_left(array, left_value)
    return right_idx - left_idx

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_x(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)

"""
7 2
1 1 2 2 2 2 3

출력: 4
"""

"""
7 4
1 1 2 2 2 2 3

출력: -1
"""