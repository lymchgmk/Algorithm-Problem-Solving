import sys
sys.stdin=open("5203_베이비진 게임.txt")

def bj_run(deck):
    for idx in range(len(deck)-3):
        if deck[idx]>=1 and deck[idx+1]>=1 and deck[idx+2]>=1:
            return True
    return False

def bj_triplet(deck):
    for num in deck:
        if num >= 3:
            return True
    return False

def bj_check(player):
    check_deck=[0]*11
    for card in player:
        check_deck[card]+=1

    if bj_triplet(check_deck) or bj_run(check_deck):
        return True
    else:
        return False

T=int(input())

for test_case in range(1, T+1):
    cards=list(map(int, input().split()))

    player1=[]
    player2=[]
    answer=0
    for i in range(len(cards)):
        if i%2==0:
            player1.append(cards[i])
            if bj_check(player1):
                answer=1
                break
        else:
            player2.append(cards[i])
            if bj_check(player2):
                answer=2
                break

    print(f'#{test_case} {answer}')