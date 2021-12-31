import sys
sys.stdin = open("1629_곱셈.txt", "rt")


def power(a, b):
    if b == 1:
        return a % C
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return (temp ** 2) % C
        else:
            return ((temp ** 2) * a) % C


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)