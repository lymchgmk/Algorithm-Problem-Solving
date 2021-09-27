def solution(sizes):
    res_w, res_h = 0, 0
    for size in sizes:
        w, h = sorted(size)
        res_w, res_h = max(res_w, w), max(res_h, h)
    return res_w * res_h


if __name__ == "__main__":
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))