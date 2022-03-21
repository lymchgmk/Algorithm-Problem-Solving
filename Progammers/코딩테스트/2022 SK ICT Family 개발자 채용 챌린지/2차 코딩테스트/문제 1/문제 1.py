import sys
import re


def make_subword(word, size):
    _subwords = set()
    for i in range(len(word) - size + 1):
        _subwords.add(word[i:i+size])
    return _subwords


def search(subword, word, goods):
    if re.search(subword, word):
        for good in goods:
            if good != word and re.search(subword, good):
                return False
        else:
            return True
    else:
        return False


def solution(goods):
    result = {good: "None" for good in goods}
    for word in goods:
        size = 1
        while size <= len(word):
            subwords = make_subword(word, size)
            tmp = []
            for subword in subwords:
                if search(subword, word, goods):
                    tmp.append(subword)
            if tmp:
                tmp.sort()
                result[word] = ' '.join(tmp)
                break
            size += 1

    print(result)
    answer = []
    for val in result.values():
        answer.append(val)
    return answer


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    goods = ["ab", "ac"]
    # goods = input()
    solution(goods)