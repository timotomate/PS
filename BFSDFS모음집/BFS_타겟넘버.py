# DFS(https://blog.naver.com/masonmount323/222774777439)
def solution(numbers, target):
    tree = [0]
    for num in numbers :
        node = []
        for i in tree :
            node.append(i+num)
            node.append(i-num)
        tree = node
    return tree.count(target)

# BFS(https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS)
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()

    n = len(numbers)

    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


numbers = [4, 1, 2, 1]
target = 4