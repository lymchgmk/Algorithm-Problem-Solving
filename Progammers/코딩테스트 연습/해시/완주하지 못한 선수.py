import collections

def solution(participant, completion):
    answer = collections.Counter(participant)
    answer.subtract(completion)
    print(answer)
    print(answer.popitem())
    print(answer.popitem())
    return answer.most_common(1)[0][0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))