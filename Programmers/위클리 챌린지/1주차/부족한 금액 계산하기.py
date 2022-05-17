def solution(price, money, count):
    total_price = (count * (count + 1) // 2) * price
    result = total_price - money
    return result if result >= 0 else 0