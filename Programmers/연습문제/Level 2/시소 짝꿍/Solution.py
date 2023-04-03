from collections import defaultdict


def solution(weights):
    answer = 0
    info = defaultdict(int)

    for w in weights:
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        info[w] += 1
        
    return answer


if __name__ == "__main__":
    weights = [100,180,360,100,270]
    result = 4
    answer = solution(weights)
    print(f"[{answer == result}] {answer}")
