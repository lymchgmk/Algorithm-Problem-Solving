import sys
sys.stdin = open("1043_거짓말.txt", "r")


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    n, m = map(int, input().split())
    knowList = set(input().split()[1:])
    parties = []

    for _ in range(m):
        parties.append(set(input().split()[1:]))

    for _ in range(m):
        for party in parties:
            if party & knowList:
                knowList = knowList.union(party)

    cnt = 0
    for party in parties:
        if party & knowList:
            continue
        cnt += 1

    print(cnt)