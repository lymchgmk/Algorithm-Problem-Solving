from collections import deque


def solution(n, m, section):
    deq = deque(section)
    count = 0

    while deq:
        curr = deq.popleft()
        count += 1

        while deq and deq[0] < curr + m:
            deq.popleft()

    return count


if __name__ == "__main__":
    n = 8
    m = 4
    section = [2, 3, 6]
    result = 2
    answer = solution(n, m, section)
    print(answer, answer == result)
