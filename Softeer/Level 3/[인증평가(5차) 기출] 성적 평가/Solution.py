import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N = int(input())
    answer = [0] * N
    for _ in range(3):
        contest = list(map(int, input().split()))
        tmp = sorted(contest, reverse=True)
        for idx, point in enumerate(contest):
            print(tmp.index(point) + 1, end=" ")
            answer[idx] += point
        print()

    for total_point in answer:
        print(answer.index(total_point) + 1, end=" ")
