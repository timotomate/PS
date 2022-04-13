def FCFS(jobs):
    now = 0
    total_time = 0
    process_time = []
    
    while jobs:
        job = jobs.pop(0)
        if job[0] >= now:
            now = job[0] + job[1]
            total_time = job[1]
            process_time.append(total_time)
        else:
            now += job[1]
            total_time = now - job[0]
            process_time.append(total_time)

    answer = sum(process_time) / 3
    
    return answer

def SJF(jobs):
    process_time = []

    job = jobs.pop(0)
    now = job[0]
    total_time = job[1]

    jobs.sort(key = lambda x: x[1])

    while jobs:
        job = jobs.pop(0)
        if job[0] >= now:
            now = job[0] + job[1]
            total_time = job[1]
            process_time.append(total_time)
        else:
            now += job[1]
            total_time = now - job[0]
            process_time.append(total_time)
    answer = sum(process_time) / 3

    return answer
