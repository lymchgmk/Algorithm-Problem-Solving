def solution(absolutes, signs):
    answer = 0
    for abs, sign in zip(absolutes, signs):
        answer += (abs if sign else -abs)
    return answer


absolutes = [4, 7, 12]
signs = [True, False, True]