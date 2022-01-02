import json
from pprint import pprint

import requests


BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
X_AUTH_TOKEN = "4287df13255bb21b19ea970587f9c982"


def start_API(PROBLEM_NUM):
    START_URL = BASE_URL + "/start"
    START_HEADER = {"X-Auth-Token": X_AUTH_TOKEN, "Content-Type": "application/json"}
    START_PROBLEM = {"problem": PROBLEM_NUM}
    response = requests.post(url=START_URL, headers=START_HEADER, data=json.dumps(START_PROBLEM))
    print(f'START_API:', response.status_code)
    print(f'START_API:', response.json())
    print()
    return response.json()["auth_key"]


def locations_API(AUTH_KEY):
    print(f'AUTH_KEY:', AUTH_KEY)
    URL = BASE_URL + "/locations"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}

    response = requests.get(url=URL, headers=HEADERS)
    print(f'LOCATIONS_API:', response.status_code)
    print(f'LOCATIONS_API:', response.json())
    print()
    return response.json()["locations"]


def trucks_API(AUTH_KEY):
    URL = BASE_URL + "/trucks"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}

    response = requests.get(url=URL, headers=HEADERS)
    print(f'TRUCKS_API:', response.status_code)
    print(f'TRUCKS_API:', response.json())
    print()
    return response.json()["trucks"]


def simulate_API(AUTH_KEY, commands):
    URL = BASE_URL + "/simulate"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}
    DATA = json.dumps({"commands": commands})

    response = requests.put(url=URL, headers=HEADERS, data=DATA)
    print(f'SIMULATE_API:', response.status_code)
    print(f'SIMULATE_API:', response.json())
    print()
    return response.json()["trucks"]


if __name__ == "__main__":
    AUTH_KEY = start_API(1)
    locations = locations_API(AUTH_KEY)
    trucks = trucks_API(AUTH_KEY)
    commands = {"truck_id": 0, "command": [2, 5, 4, 1, 6]}
    simulate_API(AUTH_KEY, commands)
