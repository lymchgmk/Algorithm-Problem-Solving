def solution(width, height, diagonals):
    for dr, dc in diagonals:
        arr = [[0] * (width+2) for _ in range(height+2)]
        diagonal_check = [[False] * (width+2) for _ in range(height+2)]
        diagonal_check[dr][dc+1] = True
        diagonal_check[dr+1][dc] = True
        start = [1, 1]
        arr[1][1] = 1
        for a in arr:
            print(a)
        print()

        for a in diagonal_check:
            print(a)
        print()

        for r in range(1, dr+2):
            for c in range(1, dc+2):
                if [r, c] == start or [r, c] == [dr+1, dc+1]:
                    continue
                print("rc", r, c)
                arr[r][c] = arr[r-1][c] + arr[r][c-1]

        arr[dr][dc+1], arr[dr+1][dc] = arr[dr+1][dc], arr[dr][dc+1]

        print("step1")
        for a in arr:
            print(a)
        print()


        for r in range(dr+1, height + 2):
            for c in range(dc+1, width + 2):
                print(r, c)
                for a in arr:
                    print(a)
                print()
                arr[r][c] = arr[r-1][c] + arr[r][c-1]



if __name__ == "__main__":
    # tc 1
    width = 2
    height = 2
    diagonals = [[1,1],[2,2]]
    print(solution(width, height, diagonals))

    # tc 2
    # width = 51
    # height = 37
    # diagonals = [[17,19]]
    # print(solution(width, height, diagonals))