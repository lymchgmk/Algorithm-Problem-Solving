import sys
sys.stdin=open("17136_색종이 붙이기.txt")

def DFS(depth):
    global my_min
    if depth >= my_min:
        return

    # 1 찾기
    for r in range(10):
        for c in range(10):
            if my_map[r][c]:
                break
        else:
            continue
        break
    else:  # 모두 0
        # 결과 갱신
        if depth < my_min:
            my_min = depth
        return

    # 붙여야 할 좌표 찾음(r, c)
    for size in range(1, 6):
        if papers[size]:  # 사이즈의 종이가 있으면
            for y in range(size):
                for x in range(size):
                    # 붙이지 못할 때 탈출
                    if not(r + y < 10 and c + x < 10 and my_map[r + y][c + x]):
                        break
                else:  # 한줄 탐색 성공
                    continue
                break
            else:  # 붙이기 성공
                # 붙이기
                papers[size] -= 1
                for y in range(size):
                    for x in range(size):
                        my_map[r + y][c + x] = 0
                DFS(depth + 1)
                # 떼기
                for y in range(size):
                    for x in range(size):
                        my_map[r + y][c + x] = 1  # 원상 복구
                papers[size] += 1  # 원상 복구
        # 다음 사이즈도 확인

my_map = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
my_min = float('inf')
DFS(0)
print(-1 if my_min == float('inf') else my_min)