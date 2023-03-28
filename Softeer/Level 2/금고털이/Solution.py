import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline

    W, N = map(int, input().split())
    metal = [tuple(map(int, input().split())) for _ in range(N)]
    metal.sort(key=lambda x: x[1], reverse=True)

    total_value: float = 0
    for Mi, Pi in metal:
        if W > Mi:
            total_value += Mi * Pi
            W -= Mi
        else:
            total_value += W * Pi
            break

    print(total_value)
