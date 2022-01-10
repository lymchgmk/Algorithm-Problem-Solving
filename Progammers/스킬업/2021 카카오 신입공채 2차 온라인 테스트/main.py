import json
from pprint import pprint
import API
import Algorithm
import history
from collections import Counter


def set_auth_key(problem_num):
    return API.start(problem_num)


if __name__ == "__main__":
    history
    # problem_num = 1
    # AUTH_KEY = set_auth_key(problem_num)
    # algorithm = Algorithm.Solution()
    #
    # for time in range(720):
    #     print(f"Time: {time}")
    #     locations = API.locations(AUTH_KEY)
    #     trucks = API.trucks(AUTH_KEY)
    #     commands = algorithm.make_commands(locations, trucks)
    #     print(locations)
    #     print(trucks)
    #     # commands = [{"truck_id": 0, "command": [0, 0, 0, 0, 0]}]
    #     response = API.simulate(AUTH_KEY, commands)
    #     if response["status"] == "finished":
    #         break
    #
    # API.score(AUTH_KEY)

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

