def solution(numbers):
    answer = []

    for number in numbers:
        binary = bin(number)[2:]
        n = 0
        while 2 ** n - 1 < len(binary):
            n += 1

        binary = '0' * (2 ** n - 1 - len(binary)) + binary
        left = bin(int(binary, 2) << 1)[2:]
        right = bin(int(binary, 2) >> 1)[2:]

        print(binary)
        print(left, bin(int(binary, 2) & int(left, 2))[2:])
        print(right, bin(int(binary, 2) & int(right, 2))[2:])

    return answer


if __name__ == "__main__":
    numbers = [7, 42, 5]
    result = [1, 1, 0]
    print(solution(numbers))