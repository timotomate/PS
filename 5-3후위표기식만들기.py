import sys
# sys.stdin = open("input.txt", "r")

a = list(input())
answer = []
stack = []



book = {"(" : 0, "+" : 1, "-" : 1 , "/" : 2, "*" : 2}


for i in a:
    if i.isdigit():
        answer.append(i)
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack[-1] != "(":
            answer.append(stack.pop())
        stack.pop()
    elif len(stack) == 0:
        stack.append(i)
    elif book[stack[-1]] < book[i]:
        stack.append(i)
    elif book[stack[-1]] >= book[i]:
        while stack and book[stack[-1]] >= book[i]:
            answer.append(stack.pop())
        stack.append(i)
    # print(i, answer, stack)

if len(stack) != 0:
    while len(stack) != 0:
        answer.append(stack.pop())

for i in answer:
    print(i, end='')