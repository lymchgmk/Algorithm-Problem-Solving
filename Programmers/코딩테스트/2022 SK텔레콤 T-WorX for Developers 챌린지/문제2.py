def solution(periods, payments, estimates):
    answer = [0, 0]
    for period, payment, estimate in zip(periods, payments, estimates):
        currVIP, postVIP = isCurrVIP(period, payment), isPostVIP(period, payment, estimate)
        if not currVIP and postVIP:
            answer[0] += 1
        if currVIP and not postVIP:
            answer[1] += 1
    return answer

def isCurrVIP(period, payment):
    sum_payment = sum(payment)
    if (period >= 60 and sum_payment >= 600000) or (period >= 24 and sum_payment >= 900000):
        return True
    else:
        return False

def isPostVIP(period, payment, estimate):
    payment.append(estimate)
    sum_payment = sum(payment[1:])
    if (period + 1 >= 60 and sum_payment >= 600000) or (period + 1 >= 24 and sum_payment >= 900000):
        return True
    else:
        return False


if __name__ == "__main__":
    period = [20, 23, 24]
    payments = 
    estimates = 
    print(solution(periods, payments, estimates))