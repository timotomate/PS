from collections import deque

priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    answer = priorities[location]

    queue = deque(priorities)
    top_prior = max(queue)
    cnt = 0

    while queue:
        if queue[0] < top_prior:
            a = queue.popleft()
            queue.append(a)
        else:
            a = queue.popleft()
            cnt += 1
            top_prior = max(queue)
            if a == answer:
                return cnt



print(solution(priorities, location))            