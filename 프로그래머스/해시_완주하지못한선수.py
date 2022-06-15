from collections import Counter

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

a = Counter(participant)
b = Counter(completion)
print(a)
print(b)
print(a-b)
print(list((a-b).keys()))
print(list((a-b).elements()))

"""
import collections

def solution(participant, completion):
    answer = []
    ct1 = collections.Counter(participant)
    ct2 = collections.Counter(completion)
    a = list((ct1-ct2).elements())
    answer = a[0]
    return answer

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]
"""