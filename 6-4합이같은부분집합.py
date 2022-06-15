import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum):




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)