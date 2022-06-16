def solution(array, commands):
    answer = []
    for a, b, c in commands:
        new_arr = array[a - 1 : b]
        new_arr.sort()
        answer.append(new_arr[c-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))