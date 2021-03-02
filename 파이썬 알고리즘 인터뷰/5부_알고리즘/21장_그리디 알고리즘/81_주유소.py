from typing import List


# 풀이 1. 모두 방문
def conCompleteCircuit_1(self, gas: List[int], cost: List[int]) -> int:
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas) + start):
            index = i % len(gas)
            
            can_travel = True
            if gas[index] + fuel < cost[index]:
                can_travel = False
                break
            else:
                fuel += gas[index] - cost[index]
        
        if can_travel:
            return start
    
    return -1


# 풀이 2. 한 번 방문
def conCompleteCircuit_2(self, gas: List[int], cost: List[int]) -> int:
    