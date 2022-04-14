"""
1. 아이디어
- 2중 for문
- BFS 돌면서 그림 갯수 +1, 최대값을 갱신

2. 시간복잡도
- O(V+E)
- V : 500 * 500
- E : 4* 500 * 500
- V + E : 5 * 250000 = 100만 < 2억 따라서 가능

3. 자료구조
- 그래프 전체 지도
- 방문했는지 여부를 위한 그래프
"""

from collections import deque
import sys

sys.stdin = open("input.txt", "r")

# n 행(x좌표) m 열(y좌표)
n, m = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]



def bfs(x, y):
    # 그림크기 = size
    size = 1
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    # 시작노드를 방문처리하고 큐에 삽입
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if image[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size


cnt = 0
maxv = 0

for i in range(n):
    for j in range(m):
        if image[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            cnt += 1
            maxv = max(maxv, bfs(i, j))

print(cnt)