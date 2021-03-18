def solution(expression):
    def calc(p, n, expression):
        if n == 2:
            return str(eval(expression))
        else:
            res = eval(p[n].join([calc(p, n+1, e) for e in expression.split(p[n])]))
            return str(res)

    priorities = [
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('-', '+', '*'),
        ('-', '*', '+'),
        ('+', '*', '-'),
        ('+', '-', '*'),
    ]
    
    answer = 0
    for p in priorities:
        res = int(calc(p, 0, expression))
        answer = max(answer, abs(res))
    return answer


expression = "100-200*300-500+20"
print(solution(expression))