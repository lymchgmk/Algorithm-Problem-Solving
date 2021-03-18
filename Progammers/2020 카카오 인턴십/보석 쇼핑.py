import collections


def solution(gems):
    L = len(gems)
    ALL_GEMS = len(set(gems))
    answer = [0, L-1]
    left, right = 0, 0
    gem_dict = {gems[0]: 1}
    while left < L and right < L:
        if len(gem_dict) == ALL_GEMS:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[1]] == 0:
                    del gem_dict[gems[left]]
                left += 1
        else:
            right += 1
            if right == ALL_GEMS:
                break
            else:
                gem_dict[gems[right]] = g
            
    


gems = ['DIA', 'EM', 'EM', 'RUB', 'DIA']
print(solution(gems))