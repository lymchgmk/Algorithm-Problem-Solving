import sys
sys.stdin=open("17136_색종이 붙이기.txt")

my_map = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]

    # 1 찾기
for r in range(10):
    for c in range(10):
        print('test', r, c)
        if my_map[r][c]:
            break
        else:
            print('else', r, c)
            continue
    break