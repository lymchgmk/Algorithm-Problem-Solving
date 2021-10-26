from itertools import permutations


def solution(k, dungeons):
    L = len(dungeons)
    answer = 0
    for perms in permutations(dungeons, L):
        tmp_k, cnt = k, 0
        for req, cost in perms:
            if tmp_k >= req and tmp_k >= cost:
                cnt += 1
                tmp_k -= cost
            else:
                break
        answer = max(answer, cnt)
    return answer


if __name__ == "__main__":
    # tc 1
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    # ans 3
    print(solution(k, dungeons))
