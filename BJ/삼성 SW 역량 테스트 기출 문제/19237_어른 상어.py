import sys
sys.stdin = open("19237_어른 상어.txt", "r")

N, M, k = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(N)]
jaws_moves = sys.stdin.readlines()
move_data = []
for i in range(len(jaws_moves)):
    move_data.append(jaws_moves[i])


print(move_data)