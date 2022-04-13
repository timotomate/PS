# zip 함수
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p!=c:
            return p

    return participant[-1]


# Counter함수
from collections import Counter

def solution(participant, completion):

    result = Counter(participant) - Counter(completion)
    
    return list(result.keys())[0]