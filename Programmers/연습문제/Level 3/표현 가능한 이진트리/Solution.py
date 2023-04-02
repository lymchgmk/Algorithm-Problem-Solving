from collections import deque
from math import floor


def solution(numbers):

    def get_padded_binary(number):
        binary = bin(number)[2:]

        n = 0
        while 2 ** n - 1 < len(binary):
            n += 1

        return ['0' * (2 ** n - 1 - len(binary)) + binary,
                binary + '0' * (2 ** n - 1 - len(binary)),
                n]

    def is_valid(binary, height):
        start_index = len(binary) // 2

        if binary[start_index] == "0":
            return False

        dq = deque([(start_index, 0)])
        visited = [False] * len(binary)
        visited[start_index] = True

        while dq:
            index, depth = dq.popleft()
            diff = floor(2 ** (height - depth - 2))
            left = index - diff
            right = index + diff

            if 0 <= left < len(binary) and not visited[left]:
                if binary[index] == "0" and binary[left] == "1":
                    return False

                visited[left] = True
                dq.append((left, depth + 1))

            if 0 <= right < len(binary) and not visited[right]:
                if binary[index] == "0" and binary[right] == "1":
                    return False

                visited[right] = True
                dq.append((right, depth + 1))

        return True

    answer = []

    for number in numbers:
        left_padded_binary, right_padded_binary, height = get_padded_binary(number)

        if is_valid(left_padded_binary, height):
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == "__main__":
    numbers = [63, 111, 95]
    result = [1, 1, 0]
    print(solution(numbers))
