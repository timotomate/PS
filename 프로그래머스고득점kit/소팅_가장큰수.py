def solution(numbers):
    if len(numbers) == numbers.count(0): return '0'
    numbers.sort(key = lambda x:str(x) * 3, reverse = True)
    return ''.join(list(map(str, numbers)))