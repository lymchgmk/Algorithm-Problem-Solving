class Boxer:
    def __init__(self, num, weight):
        self.num = num
        self.weight = weight
        self.fight_num = 0
        self.wins = 0
        self.win_rate = 0
        self.p4p = 0

def solution(weights, head2head):
    Boxers = {idx: Boxer(idx+1, weight) for idx, weight in enumerate(weights)}
    N = len(weights)
    for i in range(N):
        for j in range(i+1, N):
            if head2head[i][j] == 'W':
                Boxers[i].fight_num += 1
                Boxers[j].fight_num += 1
                Boxers[i].wins += 1
                if Boxers[i].weight < Boxers[j].weight:
                    Boxers[i].p4p += 1
            elif head2head[i][j] == 'L':
                Boxers[i].fight_num += 1
                Boxers[j].fight_num += 1
                Boxers[j].wins += 1
                if Boxers[i].weight > Boxers[j].weight:
                    Boxers[j].p4p += 1
            else:
                continue

    for idx in range(N):
        if Boxers[idx].fight_num != 0:
            Boxers[idx].win_rate += Boxers[idx].wins / Boxers[idx].fight_num

    results = [(Boxers[idx].win_rate, Boxers[idx].p4p, Boxers[idx].weight, Boxers[idx].num) for idx in range(N)]
    results.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    return [result[-1] for result in results]

if __name__ == "__main__":
    # weights = [50,82,75,120]
    # head2head =["NLWL","WNLL","LWNW","WWLN"]
    # print(solution(weights, head2head))

    # weights = [145,92,86]
    # head2head = ["NLW","WNL","LWN"]
    # print(solution(weights, head2head)) # [2, 3, 1]

    weights = [60,70,60]
    head2head = ["NNN","NNN","NNN"]
    print(solution(weights, head2head)) # [2, 1, 3]


