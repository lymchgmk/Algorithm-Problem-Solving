def solution(s, skip, index):
    answer = ''

    for char in s:
        for i in range(index):
            char = int2chr(ord(char) + 1)
            while char in set(skip):
                char = int2chr(ord(char) + 1)

        answer += char

    return answer


def int2chr(num):
    return chr((num - ord('a')) % 26 + ord('a'))


if __name__ == "__main__":
    s = "aukks"
    skip = "wbqd"
    index = 5
    result = "happy"
    answer = solution(s, skip, index)
    print(answer, answer == result)
