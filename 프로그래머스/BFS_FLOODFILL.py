from collections import deque

def BFS(i, j, image, visited, n, m):
    answer = 0
    queue = deque()
    queue.append((i, j))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        target_color = image[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == False and image[nx][ny] == target_color:
                visited[nx][ny] = True
                queue.append((nx, ny))

def solution(n, m, images):
    visited = [[False] * m for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                visited[i][j] = True
                BFS(i, j, images, visited, n, m)
                answer += 1
    return answer