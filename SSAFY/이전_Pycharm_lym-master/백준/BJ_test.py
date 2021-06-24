import sys
sys.stdin = open("BJ_test.txt")

def split_team(team):
    L= len(team)

    team1 = team[:L//2 + 1]
    team2 = team[L//2 + 1 :]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

# 플레이어 정보 가공
    players = [[player+1, card] for player, card in enumerate(cards)]


