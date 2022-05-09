import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
temp = list(range(1, n + 1))
queue = deque(temp)

while len(queue) != 1:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    queue.popleft()
print(queue[-1])

