import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
data = [] # 초기 맵
temp = [[0] * m for _ in range(n)] # 임시 변수

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1 ,1, 0, 0]

result = 0

# 사방으로 바이러스 퍼지게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 점수 얻기
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count == 3:
        # 벽 3개 세웠으면
        # 1. 임시변수 temp랑 data랑 같게 만듬
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 2. virus노드에서 virus 퍼지게 하기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)