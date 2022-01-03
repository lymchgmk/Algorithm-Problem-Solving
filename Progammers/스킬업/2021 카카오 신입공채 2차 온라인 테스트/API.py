import json
import requests


BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
X_AUTH_TOKEN = "4287df13255bb21b19ea970587f9c982"


def start(problem_num):
    URL = BASE_URL + "/start"
    HEADERS = {"X-Auth-Token": X_AUTH_TOKEN, "Content-Type": "application/json"}
    DATA = json.dumps({"problem": problem_num})

    response = requests.post(url=URL, headers=HEADERS, data=DATA)
    # print(f'START_API:', response.status_code)
    # print(f'START_API:', response.json())
    # print()
    return response.json()["auth_key"]


def locations(AUTH_KEY):
    URL = BASE_URL + "/locations"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}

    response = requests.get(url=URL, headers=HEADERS)
    # print(f'LOCATIONS_API:', response.status_code)
    # print(f'LOCATIONS_API:', response.json())
    # print()
    return response.json()["locations"]


def trucks(AUTH_KEY):
    URL = BASE_URL + "/trucks"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}

    response = requests.get(url=URL, headers=HEADERS)
    # print(f'TRUCKS_API:', response.status_code)
    # print(f'TRUCKS_API:', response.json())
    # print()
    return response.json()["trucks"]


def simulate(AUTH_KEY, commands):
    URL = BASE_URL + "/simulate"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}
    DATA = json.dumps({"commands": commands})

    response = requests.put(url=URL, headers=HEADERS, data=DATA)
    print(f'SIMULATE_API:', response.status_code)
    print(f'SIMULATE_API:', response.json())
    print()
    return response.json()


def score(AUTH_KEY):
    URL = BASE_URL + "/score"
    HEADERS = {"Authorization": AUTH_KEY, "Content-Type": "application/json"}

    response = requests.get(url=URL, headers=HEADERS)
    print(f'SCORE_API:', response.status_code)
    print(f'SCORE_API:', response.json())
    print()
