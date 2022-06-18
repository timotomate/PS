def solution(n):
    arr = [1, 2]
        
    for i in range(2, n):
        arr.append((arr[i - 1] + arr[i - 2]) % 1000000007)
        
    return arr[-1]