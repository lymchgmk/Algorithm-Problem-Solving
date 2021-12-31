import sys


sys.stdin = open('1076_저항.txt', 'rt')
ohm_dict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

answer = ''
for _ in range(2):
    answer += str(ohm_dict[input()])

for _ in range(1):
    answer = int(answer) * (10**ohm_dict[input()])
print(answer)