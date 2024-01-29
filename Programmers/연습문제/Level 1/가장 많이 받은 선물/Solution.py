from collections import Counter
from itertools import combinations


def solution(friends, gifts):
    gift_counter = {f: [Counter(), Counter()] for f in friends}
    gift_index = {f: 0 for f in friends}
    GIVE, TAKE = 0, 1
    for gift in gifts:
        giver, taker = gift.split(" ")
        gift_counter[giver][GIVE][taker] += 1
        gift_counter[taker][TAKE][giver] += 1
        gift_index[giver] += 1
        gift_index[taker] -= 1

    gift_next_month = Counter()
    for a, b in combinations(friends, 2):
        if (gift_counter[a][GIVE][b] == 0 and gift_counter[b][GIVE][a] == 0) or (
                gift_counter[a][GIVE][b] == gift_counter[b][GIVE][a]):
            if gift_index[a] < gift_index[b]:
                gift_next_month[b] += 1
            elif gift_index[b] < gift_index[a]:
                gift_next_month[a] += 1
        else:
            if gift_counter[a][GIVE][b] < gift_counter[b][GIVE][a]:
                gift_next_month[b] += 1
            elif gift_counter[a][GIVE][b] > gift_counter[b][GIVE][a]:
                gift_next_month[a] += 1

    if len(gift_next_month.most_common()) == 0:
        return 0
    else:
        return gift_next_month.most_common()[0][1]


if __name__ == "__main__":
