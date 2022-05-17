from collections import defaultdict
from math import ceil


def solution(fees, records):
    def str2time(s):
        hh, mm = map(int, s.split(':'))
        return hh * 60 + mm

    def check_io(records):
        end_time = str2time("23:59")
        io_check, total_time = dict(), defaultdict(int)
        for record in records:
            _time, _car, _io = record.split()
            _time = str2time(_time)
            if _car not in io_check:
                io_check[_car] = _time
            else:
                total_time[_car] += _time - io_check.pop(_car)
        for _car in io_check:
            total_time[_car] += end_time - io_check[_car]
        return total_time

    def calc_fee(fees, used_time):
        dft_t, dft_fee, unit_t, unit_fee = fees
        if used_time <= dft_t:
            return dft_fee
        else:
            return dft_fee + ceil((used_time - dft_t) / unit_t) * unit_fee

    used_times = check_io(records)
    used_fees = defaultdict(int)
    for _car, _time in used_times.items():
        used_fees[_car] = calc_fee(fees, _time)

    _keys = sorted(used_fees.keys())
    answer = []
    for _key in _keys:
        answer.append(used_fees[_key])
    return answer


if __name__ == "__main__":
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))