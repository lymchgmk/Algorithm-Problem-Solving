def solution(scores):
    sums = list(map(lambda x: sum(x), scores))
    wanho = sums[0]
    sorted_sums = sorted(sums[1:], reverse=True)
    min_sum = sorted_sums[-1]

    if wanho == min_sum:
        return -1

    # count = 1
    # for s_sum in sorted_sums:
    #     if s_sum <= wanho:
    #         return count
    #
    #     count += 1

    tmp = [5, 5, 4, 4, 4, 1, 1, 1]
    tmp_ans = [1, 1, 3, 3, 3, 7, 7, 7]
    wanho = 4 # 3

    check = 0
    rank = 1
    count = 0
    for s_sum in tmp:
        if s_sum > wanho:
            count += 1
            print(rank)
        elif s_sum == wanho:
            return rank
        elif s_sum < wanho:



    return -1


if __name__ == "__main__":
    scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
    result = 4
    answer = solution(scores)
    print([result == answer], answer)
