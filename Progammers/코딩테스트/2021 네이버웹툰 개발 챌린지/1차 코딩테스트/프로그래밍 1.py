from collections import Counter


def solution(S, pattern):
    _length = len(pattern)
    _counter = Counter(pattern)
    answer = 0
    for i in range(len(S)-_length+1):
        if Counter(S[i:i+_length]) == _counter:
            answer += 1
    return answer


# S = "ababababababa"
# pattern = "aabba"
S = 'abcde'
pattern = 'abc'
print(solution(S, pattern))