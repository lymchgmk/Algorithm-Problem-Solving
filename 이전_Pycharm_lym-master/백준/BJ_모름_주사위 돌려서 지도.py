import sys
sys.stdin = open("BJ_test.txt")

# "북 / 동쪽으로 부터 떨어진 칸의 갯수" >> 테스트 케이스로 검사할 것
# 주사위가 지도 밖으로 나간 경우 = 해당 명령 무시 + 출력 안함



def check(): # 주사위가 지도 밖으로 나간 경우 # pop해서 그냥 버리자
    if:
        return True # 밖
    else:
        return False # 안

def roll_the_dice(t): # 그냥 노가다로 짜야하나?

    if dir == 1:
        pass
    elif dir == 2:
        pass
    elif dir == 3:
        pass
    elif dir == 4:
        pass

    return dice[0]




#데이터 받음, 주사위 초기화
N, M, x, y, K = map(int, input().split())

my_map = [list(map(int, input().split())) for _ in range(N)]
roll = list(map(int, input().split())) # 4 4 4 1 3 3 3 2 # 1234 동서북남

dice = [0, 0, 0, 0, 0, 0] # 1, 2, 3, 4, 5, 6 면
dice[5] = my_map[x][y] # 문제에 "지도 위에 윗 면이 1"에 대한 테스트

while roll:
    temp = roll.pop(0)
    test_x = x + roll_the_dice(temp)
    test_y = y + roll_the_dice(temp)

    if test_y:

    else:
        roll_the_dice():
        x = test_x
        y = test_y