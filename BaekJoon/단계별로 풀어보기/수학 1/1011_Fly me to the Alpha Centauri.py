import sys
sys.stdin = open('1011_Fly me to the Alpha Centauri.txt', 'rt')


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    AU, pos, jump, pos_pow = y-x, 1, 1, 0

    while pos < AU:
        pos_pow += 1

        jump += 1
        pos += pos_pow
        if pos >= AU:
            break

        jump += 1
        pos += pos_pow
        if pos >= AU:
            break
    
    if pos > AU:
        jump -= 1
    
    print(jump)