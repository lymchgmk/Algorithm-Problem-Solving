import sys
sys.stdin = open('전화번호 목록.txt')

def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook[:-1], phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))