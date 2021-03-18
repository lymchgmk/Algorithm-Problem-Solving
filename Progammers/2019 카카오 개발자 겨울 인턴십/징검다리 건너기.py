import collections


def solution(stones, k):
    answer = 0
    _max = max(stones)
    for window_length in range(_max,  0, -1):
        window_s, window_e = 0, window_length-1
        for i in range(window_e, window_s, -1):
            if stones[i]:
                window_s = i
                window_e = i+window_length-1
                break
                
        
        
    
        
            
    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))