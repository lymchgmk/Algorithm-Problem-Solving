def solution(lottos, win_nums):
    def lotto645(_match):
        return 7 - _match if _match >= 2 else 6
    
    match = zeros = 0
    for lotto in lottos:
        if lotto == 0:
            zeros += 1
        elif lotto in win_nums:
            match += 1
    return [lotto645(match + zeros), lotto645(match)]
