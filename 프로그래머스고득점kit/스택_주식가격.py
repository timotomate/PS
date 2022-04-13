prices = [1, 2, 3, 2, 3]
# 싸발 이건 이하 못하겠다

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

print(solution(prices))