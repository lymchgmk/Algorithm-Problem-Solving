from collections import deque


def solution(rc, operations):

    def decomposition():
        nonlocal top, right, bottom, left, mid

        for r in range(max_r):
            for c in range(max_c):
                if c == 0:
                    left.append(rc[r][c])
                elif c == max_c - 1:
                    right.append(rc[r][c])
                elif r == 0 and 0 < c < max_c - 1:
                    top.append(rc[r][c])
                elif r == max_r - 1 and 0 < c < max_c - 1:
                    bottom.append(rc[r][c])
                else:
                    mid[r - 1].append(rc[r][c])

    def rotate():
        nonlocal top, right, bottom, left

        top.appendleft(left.popleft())
        right.appendleft(top.pop())
        bottom.append(right.pop())
        left.append(bottom.popleft())

    def shift_row():
        nonlocal top, right, bottom, left, mid

        left.appendleft(left.pop())
        right.appendleft(right.pop())

        mid.appendleft(top)
        bottom, top = mid.pop(), bottom

    def composition():
        nonlocal top, right, bottom, left, mid

        answer = [[0] * max_c for _ in range(max_r)]
        for r in range(max_r):
            for c in range(max_c):
                if c == 0:
                    answer[r][c] = left[r]
                elif c == max_c - 1:
                    answer[r][c] = right[r]
                elif r == 0 and 0 < c < max_c - 1:
                    answer[r][c] = top[c - 1]
                elif r == max_r - 1 and 0 < c < max_c - 1:
                    answer[r][c] = bottom[c - 1]
                else:
                    answer[r][c] = mid[r - 1][c - 1]

        return answer

    max_r, max_c = len(rc), len(rc[0])
    top, right, bottom, left = deque(), deque(), deque(), deque()
    mid = deque(deque() for _ in range(max_r - 2))

    decomposition()

    for operation in operations:
        print(operation)
        print(0, top, right, bottom, left, mid)
        if operation == "Rotate":
            rotate()
        elif operation == "ShiftRow":
            shift_row()
        print(1, top, right, bottom, left, mid)

    return composition()


if __name__ == "__main__":
    rc = [[1, 2], [3, 4]]
    operations = ["ShiftRow", "Rotate"]
    result = [[1, 2], [3, 4]]
    print(solution(rc, operations))
