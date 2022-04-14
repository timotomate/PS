n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for computer in range(n):
        if visited[computer] == False:
            DFS(n, computers, computer, visited)
            answer += 1
    return answer


def DFS(n, computers, computer, visited):
    visited[computer] = True
    
    # computer = 0, 1, 2
    # connect = 0, 1, 2
    for connect in range(n):
        if connect != computer and computers[computer][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
    
    return True

print(solution(n, computers))