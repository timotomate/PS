from collections import deque

def solution(priorities, location):
    queue = deque([v, i] for i, v in enumerate(priorities))
    """
    queue = deque(enumerate(priorities))
    # 인덱스번호와 원소 번호의 순서를 뒤바꾸기 위해서 위처럼 작성
    """
    cnt = 0

    while queue:
        item = queue.popleft()
        if queue and max(queue)[0] > item[0]:# item하나 뺴고 시작하기 때문에 queue가 비었는지 아닌지 체크하고 시작해야함
            queue.append(item) #맨 뒤로 보냄
        else:
            cnt += 1 
            if item[1] == location: #만약 출력한 원소의 인덱스가 우리가 찾는 놈이라면
                break
        
    return cnt

priorities = [1, 1, 9, 1, 1, 1]
location = 0