def solution(k, dungeons):
    cnt = 0
    while dungeons:
        # 현재 피로도로 갈 수 있는 곳
        dungeons = [d for d in dungeons if d[0] <= k]

        # 다음 갈 던전 고르기기
        next_idx, can_enter = -1, -1
        for idx, (req, cost) in enumerate(dungeons):
            tmp_k = k - cost
            tmp_can_enter = len([d for d in dungeons if d[0] <= tmp_k])
            if can_enter < tmp_can_enter:
                next_idx = idx
        print(next_idx, dungeons)
        if next_idx == -1:
            return cnt

        k -= dungeons[next_idx][1]
        cnt += 1


if __name__ == "__main__":
    # tc 1
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    # ans 3
    print(solution(k, dungeons))
