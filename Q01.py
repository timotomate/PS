import sys
sys.stdin = open("input.txt", "r")

n = int(input())
people = list(map(int, input().split()))
people.sort(reverse = True) #난 내림차순으로 품

scare_limit = people[0]
guild = [] # 길드
answer = 1 # 길드 갯수
mem = 0 # 길드원 수

for i in range(n):
    if mem < scare_limit:
        guild.append(people[i])
        mem += 1
    else:
        guild = []
        scare_limit = people[i]
        guild.append(people[i])
        mem = 1
        answer += 1


print(answer)