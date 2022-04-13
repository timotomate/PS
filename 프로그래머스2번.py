# 스택의 원리

def solution(s):
    c = 0
    for x in s:
        # stack
        if x == '(':
            c += 1
        # pop
        else:
            c -= 1
        if c < 0:
            return False

    return c == 0