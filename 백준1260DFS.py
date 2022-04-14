from collections import deque
import sys

#n 정점갯수, m 간선갯수, k 시작노드
n, m, k = map(int, input().split())


# graph = [[] for _ in range(n+1)]
# 0 번인덱스는 모조리 무시
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited_2 = [False for _ in range(n+1)]


for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1 # 정점 x에서 y까지 1이면
    graph[y][x] = 1 # 정점 y에서 x까지도 1이다


def dfs(v):
    #1. 시작노드는 방문처리한다
    visited[v] = True
    print(v, end = " ")
    #2. 시작노드와 인접하고, 아직 방문한 적 없다면 dfs 재귀호출한다
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    #1. 현재 노드를 큐에 삽입하고 방문처리
    q = deque([v])
    visited_2[v] = True
    #2. 큐가 비면 종료(큐에 삽입되는 순서가 순회 순서임)
    while q:
        #2-1. 큐에서 노드 하나를 꺼내고 출력
        x = q.popleft()
        print(x, end = ' ')
        #2-2. 해당 노드와 인접하고, 방문한 적 없는 노드들이 있다면 큐에 삽입, 방문처리
        for i in range(1, n+1):
            if graph[x][i] == 1 and visited_2[i] == False:
                q.append(i)
                visited_2[i] = True


dfs(k)
print()
bfs(k)