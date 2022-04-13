numbers = [3, 30, 34, 5, 9]
"""
key = labmda x:str(x) * 3 해주면
[333, 303030, 343434, 555, 999]
자릿수 맞추기 위한 수단임. 3대신에 다른 큰 숫자 집어넣어도 되지만 시간 쌉손해임
"""
answer = []
hint = ""

# from itertools import permutations
# numbers = list(permutations(numbers, len(numbers)))

def solution(numbers):
    numbers.sort(key = lambda x: str(x) * 3, reverse = True)
    print(numbers)
    return str(int(''.join(list(map(str, numbers)))))


# print(solution(numbers))