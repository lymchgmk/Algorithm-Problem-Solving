from collections import deque


def solution(cards1, cards2, goal):
    test = goal[:]
    card1, card2, goal = deque(cards1), deque(cards2), deque(goal)

    words = []
    while goal:
        curr_word = goal.popleft()

        if card1 and card1[0] == curr_word:
            words.append(card1.popleft())

        elif card2 and card2[0] == curr_word:
            words.append(card2.popleft())

    return "Yes" if words == test else "No"


if __name__ == "__main__":
    cards1 = ["i", "drink", "water"]
    cards2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]
    result = "Yes"
    answer = solution(cards1, cards2, goal)
    print(answer, answer == result)
