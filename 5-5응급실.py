# 응급도 같은 경우 제대로 답 출력 못 함
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

a, b = map(int, input().split())
queue = deque(list(map(int, input().split())))
answer = 0
cnt = 0
point = queue[b]


while answer != point:
    if max(queue) > queue[0]:
        queue.append(queue.popleft())
    else:
        answer = queue.popleft()
        cnt += 1

# print(cnt)


import sys
from collections import deque

sys.stdin=open("input.txt", "r")

n, m=map(int, input().split())


Q = deque([(pos, val) for pos, val in enumerate(list(map(int, input().split())))])
print(Q)
cnt=0

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break
