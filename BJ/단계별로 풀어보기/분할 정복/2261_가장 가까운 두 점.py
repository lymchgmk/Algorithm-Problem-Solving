import sys
sys.stdin = open("2261_가장 가까운 두 점.txt", "rt")


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1-x2)**2 + (y1-y2)**2


def solve(coords, N):
    if N == 2:
        return dist(coords[0], coords[1])
    elif N == 3:
        return min(dist(coords[0], coords[1]), dist(coords[1], coords[2]), dist(coords[2], coords[0]))

    mid = (coords[N//2][0] + coords[N//2-1][0])//2
    d = min(solve(coords[N//2:], N//2), solve(coords[:N//2], N//2))

    short_check = []
    for subset in coords:
        if mid - subset[0] <= d:
            short_check.append(subset)
    short_check.sort(key = lambda x: x[1])

    if len(short_check) == 1:
        return d
    else:
        y_check = d
        for i in range(len(short_check) - 1):
            for j in range(i+1, len(short_check)):
                if (short_check[i][1] - short_check[j][1])**2 > d:
                    break
                elif short_check[i][0] < mid and short_check[j][0] < mid:
                    continue
                elif short_check[i][0] > mid and short_check[j][0] > mid:
                    continue
                y_check = min(y_check, dist(short_check[i], short_check[j]))
    
    return y_check


input = lambda: sys.stdin.readline().strip()
N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

coords_set = list(set(map(tuple, coords)))
if len(coords_set) != len(coords):
    print("0")
else:
    coords_set.sort()
    print(solve(coords_set, N))
