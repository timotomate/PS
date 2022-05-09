import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

# book = 기준
book = list(input())
n = int(input())


for i in range(n):
    a = deque(list(input()))
    stack = []
    while a:
        study = a.popleft()
        if study in book and study not in stack:
            stack.append(study)

    if stack == book:
        print("#%d YES"%(i + 1))
    else:
        print("#%d NO"%(i + 1))



import sys
from collections import deque
sys.stdin=open("input.txt", "r")
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

x = 7

for i in range(4):
  if i == x:
    print ('멈춰!')
    break
else:
  print ('멈출수 없습니다.')