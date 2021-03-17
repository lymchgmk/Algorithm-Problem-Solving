import collections


def solution(prices):
    answer = []
    prices = collections.deque(prices)
    while prices:
        tmp = prices.popleft()
        cnt = 0
        for price in prices:
            if tmp <= price:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))