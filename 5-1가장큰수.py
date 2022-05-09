import sys
sys.stdin=open("input.txt", "rt")

num, m=map(int, input().split())
num=list(map(int, str(num)))

stack=[]

for x in num:
    while stack and m > 0 and stack[-1] < x:
        # 1. stack이 비어 있으면 무조건 원소 추가
        # 2. 자릿 수 지울 수 있는 기회 다 써버리면 무조건 원소 추가
        # 3. stack에 자료 있고, 자릿 수 지울 수 있는 기회 있으면 원소 제거하면서 기회 -= 1
        stack.pop()
        m-=1
    stack.append(x)
if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))
print(res)

