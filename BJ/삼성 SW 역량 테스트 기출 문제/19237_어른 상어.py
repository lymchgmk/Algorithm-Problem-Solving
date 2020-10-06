import sys
sys.stdin = open('19237_어른 상어.txt', 'r')

N, M, k = map(int, input().split())
jaws_data = [list(map(int, input().split())) for _ in range(N)]
jaws_dirs = list(map(int, input().split()))
jaws_dir_priority = [list(map(int, input().split())) for _ in range(4*M)]

for z in range(N):
    print(jaws_data[z])
print()

while True:
    continue

def select_dir():
    pass

def get_out_jaws():
    pass

def odor():
    pass