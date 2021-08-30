def solution(word):
    AEIOU_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]
    digits = [AEIOU_dict[char] for char in word]
    for _ in range(5 - len(word)):
        digits.append(0)

    answer = len(word)
    for digit, weight in zip(digits, weights):
        answer += digit * weight
