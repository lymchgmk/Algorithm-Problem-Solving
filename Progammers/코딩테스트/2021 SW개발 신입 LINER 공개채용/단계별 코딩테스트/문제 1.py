from typing import List
from collections import deque, defaultdict


def solution(program: str, flag_rules: List[str], commands : List[str]) -> List[bool]:
    def is_valid(program, command, flag_rules_dict):
        # 1. 각 command의 첫 단어인 실행할 프로그램에 대한 검사
        program_name, *command = command.split()
        if program != program_name:
            return False
        
        # 2. command에 대한 검사
        command_deq = deque(command)
        while command:
            # 2-0. flag 검사
            flag_name = command_deq.popleft()
            # 2-1. flag_name 검사
            try:
                flag_argument_type = flag_rules_dict[flag_name]
                if flag_argument_type == 'NULL':
                    continue
                else:
                    command_value = command_deq.popleft()
                    if flag_argument_type == 'NUMBER':
                        if not command_value.isdecimal():
                            return False
                    elif flag_argument_type == 'STRING':
                        if not command_value.isalpha():
                            return False
            # 2-2. flag_name가 존재하지 않는 경우
            except KeyError:
                print(f'"flag_rules_dict"에서 Key: {flag_name}에 대해 KeyError가 발생했습니다!')
                return False

            return True
        
    # 0-1. flag_rules를 dict로 변환
    flag_rules_dict = {}
    for flag_rule in flag_rules:
        key, val = flag_rule.split()
        flag_rules_dict[key] = val
        
    #0-2. commands의 각 엘리먼트에 대해 정합성 검사
    answer = [is_valid(program, command, flag_rules_dict)for command in commands]
    return answer
    


program = 'line'
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -s 123 -n HI", "line fun"]
print(solution(program, flag_rules, commands))