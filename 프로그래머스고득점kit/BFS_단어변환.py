begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]



from collections import deque

def solution(begin, target, words):
    answer = 0
    # 1. 큐를 만들고, 시작 노드를 큐에 담는다
    queue = deque()
    queue.append([begin, 0])

    # 참고 : visited의 인덱스번호와 words의 인덱스 번호가 같다
    visited = [False for i in range(len(words))]
    
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                # 글자수 1개만 다른 경우 큐에 담음
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    queue.append([words[i], cnt + 1])
                    visited[i] = 1

    return answer

print(solution(begin, target, words))