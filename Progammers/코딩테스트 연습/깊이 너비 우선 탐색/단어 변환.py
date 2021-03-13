import collections


def solution(begin, target, words):
    transistable = lambda word1, word2: sum([1 if x != y else 0 for x, y in zip(word1, word2)]) == 1
    transistable_dict = dict()
    transistable_dict[begin] = set(filter(lambda w: transistable(w, begin), words))
    for w in words:
        transistable_dict[w] = set(filter(lambda x: transistable(x, w), words))

    deq = collections.deque([[begin, 0]])
    while deq:
        current_word, cnt = deq.popleft()
        if cnt > len(words):
            return 0
        for w in transistable_dict[current_word]:
            if w == target:
                return cnt + 1
            else:
                deq.append([w, cnt+1])
    
    return 0


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))