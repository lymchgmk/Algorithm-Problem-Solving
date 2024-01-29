def solution(coin, cards):
    SIZE = len(cards)
    TARGET = SIZE + 1

    shortages = {card: TARGET - card for card in cards}
    deck = cards[:SIZE // 3]

    while stack:
        curu_deck, curr_round, curr_visited, curr_coin

        if () {
            max_round = max()
        }

        #1

        #2 -1
        #2- 2

        #3

    return max_round

    print(deck)
    print(cards)
    print(shortages)


if __name__ == "__main__":
    coin = 4
    cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
    answer = 5
    result = solution(coin, cards)
    print(result, result == answer)
