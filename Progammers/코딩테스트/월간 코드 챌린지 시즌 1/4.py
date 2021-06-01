from collections import deque


def how_beauty(s):
    if s == s[0] * len(s):
        return 0

    result = 0 
    for i in range(len(s)):
        for j in range(len(s)-1, i, -1):
            if s[i] != s[j] and result < j-i:
                result = j-i
    
    return result



def solution(s):
    L = len(s)
    test = s[0]
    for i in range(L):
        subset.append(s[:i+1])
    
    return subset

s = 'baby'

print(solution(s))