from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)] # m = 행의 갯수, 세로 길이
visited =[[False] * n for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque([])
B, W = 0, 0

def BFS(x, y):
    queue.append([x, y])
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 아군이며, 방문한 적이 없다면
            if 0 <= nx < m and 0 <= ny < n and graph[x][y] == graph[nx][ny] and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            ans = BFS(i, j)
            if graph[i][j] == 'W':
                W += ans ** 2
            else:
                B += ans ** 2

print(W, B)