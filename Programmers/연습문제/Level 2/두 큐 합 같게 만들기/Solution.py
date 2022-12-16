from collections import deque


def solution(queue1, queue2):
    # 합이 홀수거나 루프에 빠지면 불가능

    # target보다 합이 크면 숫자를 빼서 합이 작은 곳에 추가 후 루프 기록
  록 target = (sum(queue1) + sum(queue2)) // 2
    deque1, deque2 = deque(queue1), deque(queue2)
    print(target)
    if


if __name__ == "__main__":
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    print(solution(queue1, queue2)) # 2