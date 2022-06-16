import sys
from collections import deque
from tokenize import Triple

sys.stdin = open("input.txt", "r")

# n = 열 갯수(가로, y 좌표) m = 행 갯수(세로, x 좌표)
n, m  = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
queue = deque([])

dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maze[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1

    return maze[n-1][m-1]

print(bfs(0, 0))