import sys
sys.stdin = open("10994_별 찍기 - 19.txt", "rt")


def solution(n):
    stars = [[' '] * (4*n-3) for _ in range(4*n-3)]

    def fill(n, idx):
        if n == 1:
            stars[idx][idx] = '*'
            return
        for i in range(idx, idx + (4*n-3)):
            stars[idx][i] = stars[idx+(4*n-3)-1][i] = stars[i][idx] = stars[i][idx+(4*n-3)-1] = '*'
        return fill(n-1, idx+2)

    fill(n, 0)

    for row in stars:
        print(''.join(row))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(solution(n))
