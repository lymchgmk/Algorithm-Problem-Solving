from typing import List
import re


def solution(program: str, flag_rules: List[str], commands: List[str]) -> List[bool]:
    def is_valid(program, command, flag_rules_dict):
        # 1. 각 command의 첫 단어인 실행할 프로그램 이름에 대한 검사
        program_name, *command = map(lambda x: x.strip(), command.split('-'))
        if program != program_name:
            return False

        # 2. command에 대한 검사
        for com in command:
            flag_name, *values = com.split()
            flag_name = '-' + flag_name
            try:
                flag_argument_type = flag_rules_dict[flag_name]
                if flag_argument_type == "NULL":
                    continue
                else:
                    if flag_argument_type in ["NUMBER", "STRING"] and len(values) != 1:
                        return False
                    else:
                        if flag_argument_type == "NUMBER":
                            pattern = re.compile('[0-9]*')
                        elif flag_argument_type == "NUMBERS":
                            pattern = re.compile('[0-9]+')
                        elif flag_argument_type == "STRING":
                            pattern = re.compile('[a-zA-Z]*')
                        elif flag_argument_type == "STRINGS":
                            pattern = re.compile('[a-zA-Z]+')
                        
                        for value in values:
                            if not re.match(pattern, value):
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
    
    # 0-2. commands의 각 엘리먼트에 대해 정합성 검사
    answer = [is_valid(program, command, flag_rules_dict) for command in commands]
    return answer


program = 'trip'
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
print(solution(program, flag_rules, commands))