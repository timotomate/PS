import sys
sys.stdin = open("input.txt", "r")

n = int(input())
answer = []
for i in range(n):
    answer.append(int(input()))

answer.sort(reverse=True)

for i in answer:
    print(i, end=" ")