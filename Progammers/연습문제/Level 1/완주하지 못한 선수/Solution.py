from collections import Counter

def solution(participant, completion):
    answer = Counter(participant)
    answer.subtract(completion)
    return answer.most_common(1)[0][0]