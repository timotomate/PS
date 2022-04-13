import sys
import time
s = time.time()

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if balls[i] != balls[j]:
            cnt += 1

print(cnt)
e = time.time()
print(e-s)