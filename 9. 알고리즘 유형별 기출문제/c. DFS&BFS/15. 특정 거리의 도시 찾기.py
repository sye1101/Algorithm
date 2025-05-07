# N: 도시의 개수
# M: 도로의 개수
# K: 거리 정보
# X: 출발 도시의 번호
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
if not check:
    print(-1)

"""
4 4 2 1
1 2
1 3
2 3
2 4

출력: 4
"""

"""
4 3 2 1
1 2
1 3
1 4

출력: -1
"""

"""
4 4 1 1
1 2
1 3
2 3
2 4

출력: 2
3
"""