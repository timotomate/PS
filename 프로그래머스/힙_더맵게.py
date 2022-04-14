scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mix = a.heappop(scoville) + (2 *a.heappop(scoville))
        a.heappush(scoville, mix)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer