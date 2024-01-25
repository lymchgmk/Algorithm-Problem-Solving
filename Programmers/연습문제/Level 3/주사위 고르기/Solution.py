from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    dices = dice
    dice_indexes = range(len(dices))
    result = []
    for first_comb in combinations(dice_indexes, len(dice_indexes) // 2):
        first_dice_indexes = set(first_comb)
        second_dice_indexes = set(dice_indexes) - first_dice_indexes
        first_point_set = calcPointSet([dices[i] for i in first_dice_indexes])
        second_point_set = calcPointSet([dices[i] for i in second_dice_indexes])

        first_wins = 0
        for first_point in first_point_set:
            first_wins += bisect_left(second_point_set, first_point)

        result.append((first_comb, first_wins / 6 ** len(dice_indexes)))

    most_win_dice_indexes = list(sorted(result, key=lambda x: x[1], reverse=True))[0][0]

    return list(map(lambda x: x + 1, most_win_dice_indexes))


def calcPointSet(dices):
    point_set = []
    for _comb in product(*[range(6) for _ in range(len(dices))]):
        _sum = 0
        for index, dice in zip(_comb, dices):
            _sum += dice[index]
        point_set.append(_sum)

    return sorted(point_set)


if __name__ == "__main__":
    dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
    # dice = [[4, 1, 1, 1, 1, 2], [2, 1, 1, 2, 2, 2]]
    result = [1, 4]
    my_answer = solution(dice)
    print(f"my_answer: {my_answer}")
    print(f"{result == my_answer}")
