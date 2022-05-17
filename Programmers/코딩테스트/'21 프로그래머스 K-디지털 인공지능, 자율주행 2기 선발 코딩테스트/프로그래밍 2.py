import datetime
import collections


def solution(purchase):
    purchase_date_money = []
    for p in purchase:
        date, money = p.split()
        Y, M, D = map(int, date.split('/'))
        date = datetime.date(Y, M, D)
        money = int(money)
        purchase_date_money.append([date, money])
    
    start_date = datetime.date(2019, 1, 1)
    now_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2019, 12, 31)
    date_dict = {}
    while start_date <= now_date <= end_date:
        date_dict[now_date] = 0
        now_date += datetime.timedelta(days=1)
    
    for d in date_dict.keys():
        for p_d, m in purchase_date_money:
            if d == p_d:
                for x in range(30):
                    d += datetime.timedelta(days=1)
                    date_dict[d] += m
    
    answer = [0, 0, 0, 0, 0]
    for date, purchase_money in date_dict.items():
        if 0 <= purchase_money < 5000:
            answer[0] += 1
        elif 5000 <= purchase_money < 10000:
            answer[1] += 1
        elif 10000 <= purchase_money < 50000:
            answer[2] += 1
        elif 50000 <= purchase_money < 100000:
            answer[3] += 1
        else:
            answer[4] += 1
    
    return answer


purchase = ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]
print(solution(purchase))