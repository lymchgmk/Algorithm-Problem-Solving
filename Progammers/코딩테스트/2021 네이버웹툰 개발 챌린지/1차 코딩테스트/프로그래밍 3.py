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


from collections import deque


def _solution(letters, k):
    answer = []
    letters = deque(letters)
    while letters:
        char = letters.popleft()
        if not answer:
            answer.append(char)
            continue
        else:
            while answer and answer[-1] < char:
                answer.pop()
            answer.append(char)
    return ''.join(answer)


letters = "zbgaj"
k = 3
print(solution(letters, k))
# print(_solution(letters, k))

COunter ( a 1 b 2)
letters = "abaabaa"
k = 3
print(solution(letters, k))
# print(_solution(letters, k))
