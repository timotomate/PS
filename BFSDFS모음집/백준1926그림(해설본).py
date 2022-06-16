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


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
chk = [[False]*m for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    #그림의 크기
    answer = 1 
    #1. 시작노드를 일단 큐에 삽입
    queue = deque()
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        #2-1. 큐에서 노드 꺼내고
        x, y = queue.popleft()
        #2-2. 해당 노드의 방문하지 않은 모든 노드를 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >= n or ny < 0 or ny >= m:
                    continue
            
            #2-3. 방문하지 않은 노드들 중에서 조건을 만족한다면,
            #큐에 삽입 + 방문처리 그리고 그림의 크기(answer) + 1
            if graph[nx][ny] == 1 and chk[nx][ny] == False:
                answer += 1
                queue.append((nx, ny)) #큐에 삽입
                chk[nx][ny] = True #방문처리
    return answer


cnt = 0 # 그림 갯수
maxv = 0 # 최대 그림 갯수


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt += 1
            maxv = max(maxv, bfs(i,j))


print(cnt)