DEFAULT_COMMAND = [{"truck_id": 0, "command": [0]*10}]


class Solution:
    def __init__(self, problem_num):
        if problem_num == 1:
            self.SIZE = 5
            self.TRUCKS_CNT = 5
        else:
            self.SIZE = 60
            self.TRUCKS_CNT = 10

    def run(self):
        pass

    def make_commands(self, locations, trucks):
        pass