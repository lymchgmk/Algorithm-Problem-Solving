# 풀이 1. XOR 풀이
def hammingDistance(self, x: int, y: int) -> int:
    return bin(x ^ y).count('1')
