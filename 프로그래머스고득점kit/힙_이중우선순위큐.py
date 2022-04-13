import heapq
from collections import deque


def solution(operations):
    orders = deque()
    answer = []
    heapq.heapify(answer)

    for i in operations:
        if i[2] == '-':
            orders.append((i[0], int(i[2] + i[3:])))
        else:
            orders.append((i[0], int(i[2:])))
    """
    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)
        print(operator, operand)
    """
    while orders:
        order, value = orders.popleft()
        if order == "I":
            heapq.heappush(answer, value)
        
        # 큐 비어있으면 무시
        if answer == False:
            continue
        # 명렁어 1이면 최댓값 삭제
        elif answer and order == "D" and value == 1:
            answer.pop()
            heapq.heapify(answer)
        # 명렁어 -1이면 최솟값 삭제
        elif answer and order == "D" and value == -1:
            heapq.heappop(answer)
    
    # 자료구조에서 
    if answer:
        # return [answer[-1], answer[0]] 이렇게 쓰면 오류남.
        return [max(answer), min(answer)]
    else:
        return [0, 0]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)
        print(operator, operand)


#print(solution(operations))