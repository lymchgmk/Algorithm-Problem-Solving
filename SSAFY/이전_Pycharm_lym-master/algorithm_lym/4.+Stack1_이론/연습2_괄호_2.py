'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
'''
s = list()

def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":      #왼쪽 괄호
            s.append(data[i])
        elif data[i] == ")":    #오른쪽 괄호
            if len(s) == 0:
                return False
            else :
                s.pop()

    if s: return False
    else: return True

data = input()
print(check_matching(data))
