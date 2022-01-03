import json
from pprint import pprint
import API
from collections import Counter


def set_auth_key(problem_num):
    return API.start(problem_num)

def make_map(problem_num, locations):
    if problem_num == 1:
        SIZE = 5
    elif problem_num == 2:
        SIZE = 60

    MAP = [[[0, 0] for _ in range(SIZE)] for _ in range(SIZE)]

    for location in locations:
        id, cnt = location["id"], location["located_bikes_count"]
        r, c = id // SIZE, id % SIZE
        MAP[r][c][0] += cnt

    for m in MAP:
        print(m)

    return MAP


def make_commands():
    pass


if __name__ == "__main__":
    problem_num = 1
    AUTH_KEY = set_auth_key(problem_num)

    for _ in range(720):
        locations = API.locations(AUTH_KEY)
        curr_map = make_map(problem_num, locations)
        trucks = API.trucks(AUTH_KEY)
        commands = [{"truck_id": 0, "command": [0, 0, 0, 0, 0]}]
        response = API.simulate(AUTH_KEY, commands)
        if response["status"] == "finished":
            break

    API.score(AUTH_KEY)

    # with open("./Scenarios/problem2_day-1.json", "r") as f:
    #     json_data = json.load(f)
    #
    # borrow_counter, return_counter = Counter(), Counter()
    # for time in range(240):
    #     for data in json_data[str(time)]:
    #         borrow_id, return_id, ride_time = data
    #         borrow_counter[borrow_id] += 1
    #         return_counter[return_id] += 1
    # print(borrow_counter.most_common(10))
    # print(return_counter.most_common(10))

