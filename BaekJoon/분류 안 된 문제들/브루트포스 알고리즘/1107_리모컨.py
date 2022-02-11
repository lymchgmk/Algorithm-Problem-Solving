import sys
sys.stdin = open("1107_리모컨.txt", "rt")


def solution(N, broken_buttons):
    _buttons = {str(i): False if i in broken_buttons else True for i in range(10)}
    answer = abs(N - 100)
    for cand in range(1000001):
        for digit in str(cand):
            if not _buttons[digit]:
                break
        else:
            answer = min(answer, len(str(cand)) + abs(N - cand))
    return answer


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    M = int(input())
    broken_buttons = list(map(int, input().split()))
    print(solution(N, broken_buttons))

