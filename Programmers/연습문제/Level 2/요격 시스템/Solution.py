MAX = 100_000_000


def solution(targets):
    missles = 1
    interval_s, interval_e = -1, MAX
    for target_s, target_e in sorted(targets, key=lambda x: (x[0], -x[1])):
        if interval_s < target_s < interval_e or interval_s < target_e < interval_e:
            interval_s, interval_e = sorted([interval_s, interval_e, target_s, target_e])[1: 3]
        else:
            interval_s, interval_e = target_s, target_e
            missles += 1

    return missles


# def intersection(s1,s2): # s1의 시작점이 s2의 시작점보다 같거나 작은 상황
#     if s1[1] > s2[0]:
#         return (max(s1[0],s2[0]),min(s1[1],s2[1]))
#     return ()
#
#
# def solution(targets):
#     answer = 1
#     targets.sort(key=lambda x: x[0])
#     inter = [-1,1e9+1]
#     for target in targets:
#         inter = intersection(inter,target)
#         if not inter:
#             inter = target
#             answer+=1
#     return answer


if __name__ == "__main__":
    targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
    result = 3
    answer = solution(targets)
    print(answer == result, answer)
