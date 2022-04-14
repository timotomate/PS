from collections import deque
from itertools import product


# BFS
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1

    return answer


#
def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    #print(l)
    #print(list(product(*l)))
    s = list(map(sum, product( * l)))
    return s.count(target)


numbers = [4, 1, 2, 1]
target = 4


