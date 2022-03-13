import sys
sys.stdin = open('2309_일곱 난쟁이.txt', 'rt')


def solution(dwarves):
    def find_two_dwarves(dwarves):
        target = sum(dwarves) - 100
        for i in range(9):
            for j in range(9):
                if dwarves[i] + dwarves[j] == target:
                    return [i, j]

    dwarves.sort()
    result = find_two_dwarves(dwarves)
    for i in range(9):
        if i not in result:
            print(dwarves[i])


if __name__ == "__main__":
    dwarves = [int(input()) for _ in range(9)]
    solution(dwarves)
