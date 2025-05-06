from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1: # 집
            house.append((r, c))
        elif data[c] == 2: # 치킨집
            chicken.append((r, c))

candidates = list(combinations(chicken, m)) # 치킨집 조합 찾기

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        result += tmp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)