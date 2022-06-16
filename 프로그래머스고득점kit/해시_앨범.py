genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

#def solution(genres, plays):
answer = []

dic1 = {}
dic2 = {}

for i, (genre, play) in enumerate(zip(genres, plays)):
    if genre not in dic1:
        dic1[genre] = [(i, play)] #인덱스, 플레이타임
    else:
        dic1[genre].append((i, play))

    if genre not in dic2:
        dic2[genre] = play
    else:
        dic2[genre] += play

# print(dic2.items())
# print(sorted(dic2.items(), key = lambda x:x[1], reverse = True))
# print(dic1)

for (k, v) in sorted(dic2.items(), key = lambda x:x[1], reverse = True):
    for (i, p) in sorted(dic1[k], key = lambda x:x[1], reverse=True)[:2]:
        answer.append(i)