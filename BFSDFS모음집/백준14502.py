import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# 세로 n 가로 m
n, m = map(int, input().split())
maze = list(list(map(int, input().split())) for _ in range(n))
visited = [[False] * m for _ in range(n)]
queue = deque([])
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0


# 1. 벽 세우기
for x in range(n):
    for y in range(m):
        if maze[x][y] == 2:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and cnt < 3:
                    maze[nx][ny] = 1
                    cnt += 1


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maze[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = True
                maze[nx][ny] = 2

for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            bfs(i, j)


for i in range(n):
    answer += maze[i].count(0)

print(cnt)