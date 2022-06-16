from itertools import permutations
import math

def solution(numbers):
    result = []
    answer = []
    answer2 = []

    for i in range(len(numbers)):
            result.append(numbers[i])

    for i in range(1, len(numbers) + 1):
        arr = list(permutations(result, i))
        new_nums = [int(("").join(p)) for p in arr]
        answer += new_nums
    answer = list(set(answer))


    # 실전 에라토스테네스의 체
    for number in answer:
        if number < 2:
            continue
        check = True
        for i in range(2, int(math.sqrt(number))+ 1):
            if number % i == 0:
                check = False
        if check:
            answer2.append(number)
    
    return len(answer2)

numbers = "011"

for i in range(10):
    if i % 2 == 0:
        continue
    else:
        print("짝수")