survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

answer = dict()

for i in range(len(survey)):
    if choices[i] == 1 or 2 or 3:
        print(choices[i])
        answer[survey[i][0]] = answer.get(survey[i][0], 0) + choices[i]
    elif choices[i] == 5 or 6 or 7:
        choices[i]  = choices[i] - 4
        print(choices[i])
        answer[survey[i][1]] = answer.get(survey[i][1], 0) + choices[i]
print(answer)