#import sys
#sys.stdin = open("Algo1_구미_1반_임창묵.txt")

# 2. sudoku에 수를 넣어도 되는지 검사해 줄 check_sudoku 함수.
def check_sudoku(sdk, d):
    # 2-0. 9x9 격자에서 행과 열에 겹치는 수가 있는지 확인.
    row = sdk[d[0]]
    col = [row[d[1]] for row in sdk]
    for i in range(9):
        if row[i] == d[2] or col[i] == d[2]:
            return False

    # 2-1. 9x9 sudoku를 3x3격자 9개로 이루어진 것으로 생각. 입력할 수의 위치가 어느 3x3 격자 소속인지 알려줄 좌표.
    x, y = 3*(d[0] // 3), 3*(d[1] // 3)
    # 2-2. x,y 좌표를 기준으로 3x3 격자 내부를 탐색.
    for i in range(3):
        for j in range(3):
            # 2-2-(i). 3x3 격자에 겹치는 수가 있는 경우 False
            if sdk[x+i][y+j] == d[2]:
                return False
    # 2-3. 9x9 격자의 행과 열, 3x3 격자 내부에 겹치는 수가 없는 경우 True
    return True

# 1. 함수 sudoku_game input으로 받은 data를 그대로 가져와서 for문을 돌려 사용할 예정.
def sudoku_game(sdk, input_data):
    # 1-1. global count 변수에 게임 수행 횟수를 저장해서 출력할 것.
    global count
    # 1-2. d = [입력할 행, 입력할 열, 입력할 숫자]
    for d in input_data:
        # 1-3-(i). sudoku의 값이 비어있지 않으면 게임 수행 실패.
        if sdk[d[0]][d[1]] != 0:
            return
        # 1-3-(ii). sudoku의 값이 비어있는 경우.
        else:
            # 1-4. check_sudoku 함수를 만들어 사용해서 3x3 격자 안에 겹치는 수가 있는지 확인.
            # 1-4-(i). 입력할 숫자인 d[2]와 3x3 격자 안의 수들 간에 겹치지 않는 경우.
            if check_sudoku(sdk, d) is True:
                # 1-4-(i). 이어서 sudoku에 값 대입, count를 1 증가 시킴.
                sdk[d[0]][d[1]] = d[2]
                count += 1
            # 1-4-(ii). 입력할 숫자인 d[2]와 3x3 격자 안의 수들 간에 겹치는 경우.
            else:
                return

# 0. 문제에서 주어진 데이터 값 입력받음.
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    data = [list(map(int, input().split())) for _ in range(N)]

    # 3. 한 번도 수행하지 못할 경우 0을 출력해야하므로, count의 값은 0으로 초기화.
    count = 0
    # 4. sudoku_game 함수 실행.
    sudoku_game(sudoku, data)
    # 5. 출력.
    print(f'#{test_case} {count}')