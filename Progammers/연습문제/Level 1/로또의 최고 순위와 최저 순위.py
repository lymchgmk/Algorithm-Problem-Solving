def solution(lottos, win_nums):
    def lotto_645(how_match):
        return 7 - how_match if how_match >= 2 else 6
    
    how_match, zeros = 0, 0
    for lotto in lottos:
        if lotto == 0:
            zeros += 1
        elif lotto in win_nums:
            how_match += 1
    
    _min = lotto_645(how_match)
    _max = lotto_645(how_match + zeros)
    return [_max, _min]

    


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
