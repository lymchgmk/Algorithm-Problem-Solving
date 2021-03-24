def solution(n, words):
    import collections
    words_dict = collections.defaultdict(bool)
    end_chk = words[0][0]
    for idx, word in enumerate(words):
        if words_dict[word] or word[0] != end_chk:
            return [idx%n + 1, idx//n + 1]
        words_dict[word] = True
        end_chk = word[-1]

    return [0, 0]


n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))