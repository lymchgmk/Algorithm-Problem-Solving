# 1. 반복문
def Euclidean_1(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a


# 2. 재귀문
def Euclidean_2(a, b):
  r = b % a

  if r == 0:
    return a

  else:
    return Euclidean_2(r, a)