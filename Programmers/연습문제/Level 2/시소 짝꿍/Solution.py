from collections import defaultdict


def solution(weights):
    check_dict = defaultdict(lambda: 0)
    for weight in weights:
        for multiply in (1, 2, 3, 4):
            check_dict[weight * multiply] += 1

    print(check_dict)


if __name__ == "__main__":
    weights = [100,180,360,100,270]
    result = 4
    answer = solution(weights)
    print(f"[{answer == result}] {answer}")
