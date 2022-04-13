"""
1. FCFS 2. SJF
이 2가지 방법중에서 평균 낮은놈의 결과값 출력
근데 이게 아니라내? 다른 풀이들 보니까 무조건 SJF가 옳다는 식으로 진행
"""
jobs = [[0, 3], [1, 9], [2, 6]]

import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [[j[1], j[0]]])
        if len(heap) > 0 :
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1

    return answer // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))