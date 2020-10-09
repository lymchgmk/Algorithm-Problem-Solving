import sys
sys.stdin = open('19237_어른 상어.txt', 'r')

N, M, k = map(int, input().split())
jaws_array = [list(map(int, input().split())) for _ in range(N)]
jaws_dirs = list(map(int, input().split()))
dirs_priority = []
for i in range(M):
    dirs_priority.append([list(map(int, input().split())) for _ in range(4)])

print(dirs_priority)

for z in range(N):
    print(jaws_array[z])
print()

jaws_in_the_array= [True] * M

def select_dir():
    pass

def get_out_jaws():
    pass

def odor():
    pass

