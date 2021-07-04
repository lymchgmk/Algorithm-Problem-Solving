def solution(word):
    # 0-1. 알파벳 모음 AEIOU가 가지는 순서의 의미를 사용하기 위한 mapping용 dict
    AEIOU_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    # 0-2. 각 자리가 1 증가할 때마다의 경우의 수 y = 5x + 1
    weights = [781, 156, 31, 6, 1]
    # 1. word를 숫자를 가진 자릿값으로 변환
    digits = [AEIOU_dict[char] for char in word]
    # 1-1. 사전 순의 의미를 위해서 5보다 짧은 경우 0의 자릿값을 뒤에서 채워줌
    for _ in range(5 - len(word)):
        digits.append(0)

    # 2. 계산
    # 2-1. 예를 들어 길이가 4인 문자열의 경우, AAAA로 시작하는, 즉 최소 4의 기본값을 가지게 됨
    answer = len(word)
    for digit, weight in zip(digits, weights):
        answer += digit * weight
    return answer

word = "AAAAE"
print(solution(word))
word = 'AAAE'
print(solution(word))
word = 'I'
print(solution(word))
word = 'EIO'
print(solution(word))