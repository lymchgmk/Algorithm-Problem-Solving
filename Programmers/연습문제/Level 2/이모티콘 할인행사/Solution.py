from itertools import product


def solution(users, emoticons):
    discounts = (10, 20, 30, 40)
    result = [0, 0]
    for _discounts in product(discounts, repeat=len(emoticons)):
        curr_result = check(users, emoticons, _discounts)
        if result[0] < curr_result[0] or (result[0] == curr_result[0] and result[1] < curr_result[1]):
            result = curr_result

    return result


def check(users, emoticons, discounts):
    subscribe = purchased_emoticons = 0
    for discount_threshold, budget in users:
        purchased = 0
        for emoticon, discount in zip(emoticons, discounts):
            if discount_threshold <= discount:
                purchased += emoticon * (100 - discount) // 100

        if budget <= purchased:
            subscribe += 1
        else:
            purchased_emoticons += purchased

    return [subscribe, purchased_emoticons]


if __name__ == "__main__":
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    result = [4, 13860]
    print(solution(users, emoticons))
