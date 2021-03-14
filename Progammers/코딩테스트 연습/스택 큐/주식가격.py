def solution(prices):
    answer = []
    for i in range(len(prices)):
        price = prices[i]
        stack = []
        for j in range(i+1, len(prices)):
            if price <= prices[j]:
                stack.append(prices[j])
            else:
                stack.append(0)
                break
        answer.append(len(stack))
    
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))