import sys
sys.stdin = open("input.txt", "r")

# 재귀함수를 사용

def DFS(x):
    if x > 0: 
        DFS(x - 1)
        print(x, end = ' ')


if __name__=="__main__":
    n = int(input())
    DFS(n)