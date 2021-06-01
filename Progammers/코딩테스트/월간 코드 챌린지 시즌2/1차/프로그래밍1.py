def solution(absolutes, signs):
    answer = 0
    for num, tf in zip(absolutes, signs):
        if tf == 'true':
            answer += num
        else:
            answer += (-1)*num
    return answer


absolutes = [4, 7, 12]
signs = ['true', 'false', 'true']
print(solution(absolutes, signs))
