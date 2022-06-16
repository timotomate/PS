"""
1. 아이디어
- 2중 for, 값1 && 방문X => DFS
- DFS를 통해 찾은 값을 저장

2. 시간복잡도
- DFS O(V+E)
- V, E = N^2, 4N^2
- V+E = 625

3. 자료구조
- 그래프(2차원 배열)
- 방문여부 기록용 2차원 배열
- 결과값을 저장할 리스트(그림의 크기)
"""

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

chk = [[False] * n for _ in range(n)]
result = [] # 집 들
each = 0 # 집의 수

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    # 1. 시작노드 x, y는 밑의 for문에서 주어짐
    # dfs 한 바퀴 돌 때마다 단지 집 갯수 1개 추가
    global each
    each += 1
    # 2-1. 해당 노드 기준으로 4가지 방향을 살핀다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 2-2. 조건을 만족한다면(아직 방문한적이 없고, 방문 가능한 집이라면)
        # 해당 집을 방문처리한다
        # 2-3. 방문처리 후 재귀호출한다
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and chk[nx][ny] == False:
                chk[nx][ny] = True # 방문처리
                dfs(nx, ny) # 재귀 호출

        
for i in range(n):
    for j in range(n):
        # 방문할 수 있는데, 아직 방문한 적 없다면
        if graph[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True # 방문처리하고
            each = 0 # 집 갯수 초기화
            dfs(i, j)
            result.append(each)

result.sort()
print(len(result))# 총 단지 수
for i in result:
    print(i)