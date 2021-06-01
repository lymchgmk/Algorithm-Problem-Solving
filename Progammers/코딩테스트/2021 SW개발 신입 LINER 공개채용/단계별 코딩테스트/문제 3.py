from typing import List
import re
# program = 'line'
# flag_rules = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
# commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]

def solution(program: str, flag_rules: List[str], commands: List[str]) -> List[bool]:
    def is_valid(program, command, flag_rules_dict):
        # 0. ALIAS 검사 준비
        alias_dict = {a: False for a in flag_rules_dict['ALIAS']}
        
        # 1. 각 command의 첫 단어인 실행할 프로그램 이름에 대한 검사
        program_name, *command = map(lambda x: x.strip(), command.split('-'))
        if program != program_name:
            return False
        
        # 2. command에 대한 검사
        for com in command:
            flag_name, *values = com.split()
            flag_name = '-' + flag_name
            
            # 3. ALIAS 검사
            if flag_name in alias_dict:
                if len(flag_rules_dict[flag_name]) == 1:
                    if not alias_dict[flag_name]:
                        alias_dict[flag_name] = True
                    else:
                        return False
                else:
                    if alias_dict[flag_name] or alias_dict[flag_rules_dict[flag_name][1]]:
                        return False
                    else:
                        alias_dict[flag_name] = True
                        alias_dict[flag_rules_dict[flag_name][1]] = True
                
            try:
                if len(flag_rules_dict[flag_name]) != 1:
                    flag_argument_type = flag_rules_dict[flag_rules_dict[flag_name][1]]
                else:
                    flag_argument_type = flag_rules_dict[flag_name][0]
                    
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
    flag_rules_dict = {'ALIAS': []}
    for flag_rule in flag_rules:
        key, *val = flag_rule.split()
        if val[0] == 'ALIAS':
            flag_rules_dict['ALIAS'].extend([key, val[1]])
        flag_rules_dict[key] = val
    
    # 0-2. commands의 각 엘리먼트에 대해 정합성 검사
    answer = [is_valid(program, command, flag_rules_dict) for command in commands]
    return answer



program = 'line'
flag_rules = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]
print(solution(program, flag_rules, commands))