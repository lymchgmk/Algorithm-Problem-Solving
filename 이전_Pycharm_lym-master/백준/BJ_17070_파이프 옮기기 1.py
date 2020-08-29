import sys
sys.stdin = open("BJ_17070_파이프 옮기기 1.txt", "r")

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

print(house)

# stack으로 dfs 사용
# case 1, 2, 3로 나눠서 함수 실행, while (x,y) != (N, N)으로 연속
# arr에 1있는 경우는 가지치기 할 것