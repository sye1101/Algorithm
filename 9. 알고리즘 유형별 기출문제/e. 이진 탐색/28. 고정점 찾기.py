def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid: # 왼쪽인 경우
        return binary_search(array, start, mid - 1)
    else: # 오른쪽인 경우
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

result = binary_search(array, 0, len(array))

if result == None:
    print(-1)
else:
    print(result)

"""
5
-15 -6 1 3 7

출력: 3
"""

"""
7
-15 -4 2 8 9 13 157

출력: 2
"""

"""
7
-15 -4 3 8 9 13 15

출력: -1
"""