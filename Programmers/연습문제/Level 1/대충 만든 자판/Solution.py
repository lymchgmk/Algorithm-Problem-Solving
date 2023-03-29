from collections import defaultdict


def solution(keymap, targets):
    keydict = defaultdict(lambda: float('inf'))

    for _keymap in keymap:
        for cnt, key in enumerate(_keymap, start=1):
            keydict[key] = min(keydict[key], cnt)

    answer = []
    for target in targets:
        result = 0
        for char in target:
            result += keydict[char]

        if 0 < result < float('inf'):
            answer.append(result)
        else:
            answer.append(-1)

    return answer


if __name__ == "__main__":
    keymap = ["ABACD", "BCEFD"]
    targets = ["ABCD", "AABB"]
    result = [9, 4]
    answer = solution(keymap, targets)
    print(answer, answer == result)