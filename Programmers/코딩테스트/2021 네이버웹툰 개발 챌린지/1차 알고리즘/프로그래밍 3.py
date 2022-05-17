from collections import Counter


def solution(letters, k):
    _sorted = sorted(letters, reverse=True)[:k]
    _Counter = Counter(_sorted)
    answer = ''
    for i in range(len(letters)-1, -1, -1):
        letter = letters[i]
        if _Counter[letter]:
            answer = letter + answer
            _Counter[letter] -= 1
    return answer


letters = "zbgaj"
k = 3
print(solution(letters, k))


letters = "abaabaa"
k = 3
print(solution(letters, k))