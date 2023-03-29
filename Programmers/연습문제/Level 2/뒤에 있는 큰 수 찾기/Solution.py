from collections import deque

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)

    return answer


if __name__ == "__main__":
    numbers = [2, 3, 3, 5]
    result = [3, 5, 5, -1]
    answer = solution(numbers )
    print(f'[{answer == result}] {answer}')
