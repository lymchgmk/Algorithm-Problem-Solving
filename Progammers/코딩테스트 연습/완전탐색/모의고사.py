answers = [1,3,2,4,2]

def my_solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt=[0]*3
    for idx, answer in enumerate(answers):
        if supo1[idx % len(supo1)] == answer: cnt[0] += 1;
        if supo2[idx % len(supo2)] == answer: cnt[1] += 1;
        if supo3[idx % len(supo3)] == answer: cnt[2] += 1;

    answer = [ans[0] for ans in list(filter(lambda x: x[0] if x[1] == max(cnt) else 0, zip([1, 2, 3], cnt)))]
    return answer

print(my_solution(answers))