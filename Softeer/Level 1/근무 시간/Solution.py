import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    total_work_time = 0
    for _ in range(5):
        on, off = input().split()
        on_HH, on_MM = map(int, on.split(':'))
        off_HH, off_MM = map(int, off.split(':'))
        total_work_time += (off_HH - on_HH) * 60 + (off_MM - on_MM)

    print(total_work_time)