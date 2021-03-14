def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x: x[1])
    current_time = 0
    L = len(jobs)
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= current_time:
                current_time += jobs[i][1]
                answer += current_time - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs)-1:
                current_time += 1
                
    return answer // L


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
