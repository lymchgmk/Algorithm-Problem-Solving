def solution(numbers, target):
    def calcSum(idx, sum):
        nonlocal answer
        if idx == len(numbers):
            if sum == target:
                answer += 1
            return

        calcSum(idx+1, sum + numbers[idx])
        calcSum(idx+1, sum - numbers[idx])

    answer = 0
    calcSum(0, 0)
    return answer


if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 3
    result = 5
    answer = solution(numbers, target)
    print(answer == result, answer)

