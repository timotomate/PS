#DFS(음료수 만들어 먹는 방법)
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def dfs(x, y):
    # 범위 벗어났다면 바로 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 2-1. 현재 노드를 아직 방문하지 않았다면 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 2.2 상하좌우도 모두 재귀적으로 호출
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)