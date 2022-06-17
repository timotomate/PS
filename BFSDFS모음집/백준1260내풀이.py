import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# n = 정점의 갯수, m = 간선의 갯수, k = 시작노드
n, m, k = map(int, input().split())


graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)] #DFS용
visited_2 = [False for _ in range(n+1)] #BFS용

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visited[v] = True
    print(v, end = " ")
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited_2[v] = True

    while queue:
        x = queue.popleft()
        for i in range(1, n + 1):
            if graph[x][i] == 1 and visited_2[i] == False:
                queue.append(i)
                visited_2[i] = True


