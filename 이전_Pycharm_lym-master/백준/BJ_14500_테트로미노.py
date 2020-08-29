import sys
sys.stdin = open("BJ_14500_테트로미노.txt", "r")

def tetromino():
    pass

def two_by_three():
    for i in range(0, N-1):
        for j in range(0, M-2):


def three_by_two():
    for i in range(0, N-2):
        for j in range(0, M-1):





N, M = map(int, input().split()) #[4, 500]
data = [list(map(int, input().split())) for N_case in range(N)]
print(data)


# 이어서 1x4는 따로 체크 + 나머지는 2x3, 3x2로 체크 (+ 폴리오미노 체크 == 없는 박스 간 좌표가 i, j 모두 절대값 1차이 안나는 경운)
