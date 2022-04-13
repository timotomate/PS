def solution(citations):
    citations = sorted(citations)
    
    l = len(citations)
    # citations = [0, 1, 3, 5, 6]
    for i in range(l):
        if citations[i] >= l-i: 
            # citations[i] = 인용된 횟수(h)
            # l-i = 인용된 논문의 갯수를 최대값 부터 차례대로 줄여감(h)
            return l-i
    return 0