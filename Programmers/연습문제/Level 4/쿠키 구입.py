# def solution(cookie):
#     answer = 0
#     L = len(cookie)
#
#     for start in range(L - 1):
#         son_1_idx, son_2_idx = start, start + 1
#         son_1_cookies, son_2_cookies = cookie[son_1_idx], cookie[son_2_idx]
#
#         while True:
#             if son_1_cookies == son_2_cookies:
#                 answer = max(answer, son_1_cookies)
#
#             if 0 < son_1_idx and son_1_cookies <= son_2_cookies:
#                 son_1_idx -= 1
#                 son_1_cookies += cookie[son_1_idx]
#             elif son_2_idx < L - 1 and son_1_cookies >= son_2_cookies:
#                 son_2_idx += 1
#                 son_2_cookies += cookie[son_2_idx]
#             else:
#                 break
#
#     return answer


from itertools import accumulate


def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        son_1 = set(accumulate(reversed(cookie[:m+1])))
        son_2 = set(accumulate(cookie[m+1:]))
        can_give = son_1 & son_2

        if can_give:
            answer = max(*can_give, answer)
            
    return answer



n = 6
cookie = [1, 2, 3]
print(solution(cookie))
