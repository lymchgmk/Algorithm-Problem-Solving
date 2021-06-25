import re


def solution(s):
    answer = []
    for x in s:
        # 1. '110' 제거
        cnt = 0
        while True:
            post_x = re.sub(pattern=r'(110)', repl='', string=x)
            if x == post_x:
                break
            x = post_x
            cnt += 1

        print(x, cnt)
        # 2. '110' 삽입
        while cnt:
            for i in range(len(x)-1, -1, -1):
                if x[i] == '0':
                    x = x[:i+1] + '110' + x[i+1:]
                    break
            else:
                # 예외처리?
                x += '110'
            print(x)
            cnt -= 1

    return answer
        
        
s = ["1110","100111100","0111111010"]
print(solution(s))
