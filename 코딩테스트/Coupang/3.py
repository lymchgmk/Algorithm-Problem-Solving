def solution(k, score):
    score_diff = []
    for i in range(len(score)-1):
        score_diff.append(score[i] - score[i+1])
    
    score_dict = dict()
    for diff in score_diff:
        if diff not in score_dict.keys():
            score_dict[diff] = 1
        else:
            score_dict[diff] = score_dict[diff]+1
    
    temp = []
    for idx, diff in enumerate(score_dict.values()):
        if diff >= k:
            temp.append(idx)
    
    result_keys = []
    for t in temp:
        result_keys.append(list(score_dict.keys())[t])

    result_default_set = set(list(range(1, len(score)+1)))
    result_set = set()
    for idx, diff in enumerate(score_diff):
        if diff in result_keys:
            result_set.add(idx+1)
            result_set.add(idx+2)

    result = len(result_default_set - result_set)

    return result

k = 2
data = 	[1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
print(solution(k, data))