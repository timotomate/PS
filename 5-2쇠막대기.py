import sys
sys.stdin = open("input.txt", "r")

a = list(input())
stack = []
razer = 0
stick = 0

for i in a:
    if i == '(':
        stack.append(i)
    elif i == ')' and stack[-1] == '(':
        stack.pop()
        razer += 1

import sys
sys.stdin = open("input.txt", "r")

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        # 레이저
        if s[i-1]=='(': # 레이저
            cnt += len(stack)
        else: # 막대기의 끝
            cnt += 1
print(cnt)