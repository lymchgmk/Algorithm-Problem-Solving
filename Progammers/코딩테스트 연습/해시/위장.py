import collections


def solution1(clothes):
    clothes_counter = collections.Counter([cloth[1] for cloth in clothes])
    answer = 1
    for c in clothes_counter.values():
        answer *= c+1
        
    return answer-1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution1(clothes))