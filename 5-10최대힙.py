import sys
import heapq

sys.stdin = open("input.txt", "r")

arr = []

while True:
    a = int(input())

    if a == -1:
        break
    elif a == 0:
        if len(arr) == 0:
            print(-1)
        else:
            print(heapq.heappop(arr) * -1)
    else:
        heapq.heappush(arr, a * -1)