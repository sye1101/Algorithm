def count_x(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)
    if a == None:
        return 0 # x 존재하지 않음

    b = last(array, x, 0, n-1)

    return b - a + 1


def first(array, x, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or x > array[mid-1]) and array[mid] == x: # 해당 위치의 x가 처음으로 나온 x인지 확인
        return mid
    elif array[mid] >= x: # 왼쪽에 있는 경우
        return first(array, x, start, mid - 1)
    else: # 오른쪽에 있는 경우
        return first(array, x, mid + 1, end)

def last(array, x, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or x < array[mid + 1]) and array[mid] == x: # 해당 위치의 x가 마지막으로 나온 x인지 확인
        return mid
    elif array[mid] > x: # 왼쪽에 있는 경우
        return last(array, x, start, mid - 1)
    else: # 오른쪽에 있는 경우
        return last(array, x, mid + 1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_x(array, x)

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