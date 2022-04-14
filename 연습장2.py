from collections import deque


def solution(n, m, infests, vaccinateds):
    day, count = 0, len(infests)

    office = [[False] * n for _ in range(m)]

    for x, y in infests:
        office[x - 1][y - 1] = True

    for x, y in vaccinateds:
        office[x - 1][y - 1] = -1

    queue = deque()
    for x, y in infests:
        queue.append([x - 1, y - 1, 0])

    dx = [0, 0, -1 ,1]
    dy = [-1 ,1, 0, 0]

    # 현재 큐에는 0일차에 이미 감염된 놈들이 삽입되어있음.
    # [x좌표, y좌표, day = 0]
    
    while queue:
        x, y, day = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and office[nx][ny] == False:
                count += 1
                office[nx][ny] = 1
                queue.append([nx, ny, day + 1])

    if count != m * n - len(vaccinateds):
        return -1
    
    return day


m = 2
n = 4
infests= [[1, 4], [2, 2]]
vaccinateds = [[1, 2]]

print(solution(n, m, infests, vaccinateds))