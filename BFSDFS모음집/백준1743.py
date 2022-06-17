import sys
sys.stdin = open("input.txt", "r")
from collections import deque

n, m, trash = map(int, input().split())

maze = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = []

for _ in range(trash):
    x, y = map(int, input().split())
    maze[x - 1][y - 1] = "#"

queue = deque([])

def bfs(x, y):
    answer = 1
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maze[nx][ny] == "#":
                queue.append([nx, ny])
                visited[nx][ny] = True
                answer += 1
    
    return answer

maxv = 0

for i in range(n):
    for j in range(m):
        if maze[i][j] == "#" and visited[i][j] == False:
            maxv = max(maxv, bfs(i, j))

print(maxv)


