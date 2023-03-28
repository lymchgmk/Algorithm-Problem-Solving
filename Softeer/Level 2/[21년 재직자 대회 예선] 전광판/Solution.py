import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    board = {
        '0': "1110111",
        '1': "0000011",
        '2': "0111110",
        '3': "0011111",
        '4': "1001011",
        '5': "1011101",
        '6': "1111101",
        '7': "1010011",
        '8': "1111111",
        '9': "1011111"
    }

    T = int(input())
    for _ in range(T):
        A, B = input().split()
        A = ["0000000"] * (5 - len(A)) + list(map(lambda x: board[x], A))
        B = ["0000000"] * (5 - len(B)) + list(map(lambda x: board[x], B))

        result = 0
        for i in range(5):
            result += str(bin(int(A[i], 2) ^ int(B[i], 2))).count("1")

        print(result)
