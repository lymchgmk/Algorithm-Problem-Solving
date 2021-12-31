import sys
sys.stdin = open('2798_블랙잭.txt', 'rt')


N, M = map(int, input().split())
cards = list(map(int, input().split()))

chk, answer = M, 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and k != i:
                three_cards = cards[i] + cards[j] + cards[k]
                if three_cards <= M and chk > M - three_cards:
                    chk, answer = M - three_cards, three_cards

print(answer)