import json
from collections import Counter


def make_history_data(problem_json):
    cntr1, cntr2, cntr3 = Counter(), Counter(), Counter()
    for time in problem_json:
        for borrow_id, return_id, ride_time in problem_json[time]:
            if 0 <= int(time) < 240:
                cntr1[borrow_id] += 1
            elif 240 <= int(time) < 480:
                cntr2[borrow_id] += 1
            else:
                cntr3[borrow_id] += 1
    return [cntr1, cntr2, cntr3]


if __name__ == "__main__":
    with open("./Scenarios/problem1_day-1.json", "r") as f:
        problem1_day_1_data = json.load(f)
    with open("./Scenarios/problem1_day-2.json", "r") as f:
        problem1_day_2_data = json.load(f)
    with open("./Scenarios/problem1_day-3.json", "r") as f:
        problem1_day_3_data = json.load(f)
    with open("./Scenarios/problem2_day-1.json", "r") as f:
        problem2_day_1_data = json.load(f)
    with open("./Scenarios/problem2_day-2.json", "r") as f:
        problem2_day_2_data = json.load(f)
    with open("./Scenarios/problem2_day-3.json", "r") as f:
        problem2_day_3_data = json.load(f)

    make_history_data(problem1_day_1_data)
