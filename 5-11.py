#BFS
from collections import deque
import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    # 1. 시작노드를 일단 큐에 삽입
    queue.append((x, y))
    answer = 0

    # 큐가 빌 때까지 반복
    while queue:
        # 2-1. 큐에서 노드 꺼내고
        x, y = queue.popleft()
        # 2-2. 해당 노드의 모든 방향이 조건 만족한다면 큐에 삽입하고 방문처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]

print(bfs(0, 0))