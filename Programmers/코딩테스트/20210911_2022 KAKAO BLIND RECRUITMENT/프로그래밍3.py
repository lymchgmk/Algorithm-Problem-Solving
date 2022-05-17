from collections import defaultdict
from math import ceil


def calculate_fee(minutes):
    if minutes <= fees[0]:
        return fees[1]
    else:
        return fees[1] + ceil((minutes - fees[0])/fees[2]) * fees[3]


def solution(fees, records):
    parking = defaultdict(dict)
    result = defaultdict(int)
    for record in records:
        HHMM, car_num, IN_OUT = record.split()
        H, M = map(int, HHMM.split(':'))
        T = 60 * H + M
        if IN_OUT == 'IN':
            parking[car_num]['IN'] = T
            parking[car_num]['OUT'] = float('inf')
        else:
            parking[car_num]['OUT'] = T
            in_m, out_m = parking[car_num]['IN'], parking[car_num]['OUT']
            result[car_num] += out_m - in_m

    for car_num in parking:
        if parking[car_num]['OUT'] == float('inf'):
            in_m, out_m = parking[car_num]['IN'], 60 * 23 + 59
            result[car_num] += out_m - in_m

    answer = []
    for car_num, used_time in result.items():
        answer.append([car_num, calculate_fee(used_time)])

    return [ans[1] for ans in sorted(answer)]

    #     used_time = parking[car_num]['IN'] - parking[car_num]['OUT']
    #     result.append((int(car_num), calculate_fee(used_time)))
    #
    # result.sort()
    # return [r[1] for r in result]


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records)) # [14600, 34400, 5000]