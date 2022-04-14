n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for com in range(n):
        # 아직 현재 노드를 방문하지 않은 경우에
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    # com = DFS를 수행할 시작점(v, node라고 생각하면 됨)

    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 자기자신이 아니고, 자
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


# 코드출처 : https://velog.io/@timointhebush/