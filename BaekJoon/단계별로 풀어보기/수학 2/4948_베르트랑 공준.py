import sys
sys.stdin = open('4948_베르트랑 공준.txt', 'rt')

while True:
    tc = int(input())
    if tc == 0:
        break
    else:
        count = 0
        for n in range(tc+1, 2*tc+1):
            if n >= 2:
                for i in range(2, int(n**0.5 + 1)):
                    if n % i == 0:
                        break
                else:
                    count += 1
        print(count)
