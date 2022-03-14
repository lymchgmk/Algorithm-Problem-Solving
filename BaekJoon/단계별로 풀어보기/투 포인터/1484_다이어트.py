import sys
sys.stdin = open("1484_다이어트.txt", 'rt')


def solution(G):
    MAX_G = 100000
    cands = [x**2 for x in range(100001)]

    l, r = 1, 2
    answer = []
    while True:
        gap = cands[r] - cands[l]
        if r - l == 1 and gap > MAX_G:
            break

        if gap < G:
            r += 1
        elif gap > G:
            l += 1
        else:
            answer.append(r)
            l += 1

    if answer:
        for ans in answer:
            print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    input = sys.stdin.readline
    G = int(input())
    solution(G)
