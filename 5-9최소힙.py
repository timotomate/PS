import sys
import heapq

sys.stdin = open("input.txt", "r")
arr = []

while False:
    hq = heapq.heapify(arr)
    a = int(input())
    if hq and a == 0:
        print(heapq.heappop(arr))
    elif a == -1:
        break
    else:
        heapq.heappush(arr, a)