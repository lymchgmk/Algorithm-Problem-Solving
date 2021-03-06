# 풀이 1. 1의 개수 개산
def hammingWeight_1(self, n: int) -> int:
    return bin(n).count('1')


# 풀이 2. 비트 연산
def hammingWeight_2(self, n: int) -> int:
    count = 0
    while n:
        # 1을 뺀 값과 AND 연산 횟수 측정
        n &= n - 1
        count += 1
    
    return count
