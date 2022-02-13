import sys
from itertools import combinations
sys.stdin = open("1759_암호 만들기.txt", 'rt')


def solution(L, C, chars):
    chars.sort()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    passwords = []
    for comb in combinations(chars, L):
        cnt_vowels = 0
        for char in comb:
            if char in vowels:
                cnt_vowels += 1
        if cnt_vowels >= 1 and L - cnt_vowels >= 2:
            passwords.append(''.join(comb))

    for password in passwords:
        print(password)


if __name__ == "__main__":
    input = sys.stdin.readline
    L, C = map(int, input().split())
    chars = input().split()
    solution(L, C, chars)