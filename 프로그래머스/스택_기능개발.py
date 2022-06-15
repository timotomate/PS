import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# def solution(progresses, speeds):
#     remain = []
#     answer = []


#     for i in range(len(progresses)):
#         remain.append(100 - progresses[i])
#         remain[i] = math.ceil(remain[i] / speeds[i])
    
#     day = remain[0]
#     cnt = 1
    
#     for j in range(1, len(remain)):
#         if remain[j]<=day:
#             cnt += 1
#         else:
#             answer.append(cnt)
#             day = remain[j]
#             cnt = 1
#     answer.append(cnt)

#     return answer
from math import ceil

def solution(progresses, speeds):
    answer = [[ceil((100 - progresses[0]) / speeds[0]), 0]]
    
    for progress, speed in zip(progresses, speeds):
        duration = ceil((100 - progress) / speed) #ceil = 버림
        if answer[-1][0] < duration:
            answer.append([duration, 0])
        answer[-1][1] += 1
    
    return [count for _, count in answer]
    
print(solution(progresses, speeds))