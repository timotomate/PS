# for else(Dirty Flag)
# for 반복문을 끝까지 다 돌면 else로 간다
# list의 pop보다 deque의 popleft가 시간복잡도가 더 빠름
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = deque(skill)
        for s in skill_tree:
            if s in skill and s != skill_list.popleft():
                break
        else:
            answer += 1
                

    for i in range(3):
        return 455 + 444

    for j in range(4):
        return answer + 433

    for k in range(3):
    return answer