import heapq
import sys
from collections import deque
INF = int(1e9)

sys.stdin = open("input.txt", "r")

n, m, k, x = map(int, input().rstrip().split())
# 0번 인덱스 사용하지 않기 위해서 모조리 한 칸 크게 함
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

# 인접 리스트 방식으로 그래프 처리!!
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)


def bfs(graph, start, visited):
    #1. 시작 노드를 일단 큐에 삽입하고, 방문처리, 거리는 0
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    # 큐가 빌 때까지 반복
    while queue:
        # 2-1. 큐에서 노드 꺼내고
        now = queue.popleft()
        # 2-2. 해당 노드 기준으로 조건을 만족하는 노드가 있다면, 큐에 삽입하고
        # 방문처리, 거리 +1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                queue.append(i)

bfs(graph, x, visited)

if k not in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if k == distance[i]:
            print(i)