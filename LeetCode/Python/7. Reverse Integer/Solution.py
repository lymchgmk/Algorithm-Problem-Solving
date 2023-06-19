class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        rev_str_x = str_x[::-1]
        value_x = int(rev_str_x)

        if not (-(2 ** 31) <= value_x <= 2 ** 31 - 1):
            return 0

        return value_x if x >= 0 else -value_x


class Best_Solution:
    def reverse(self, x: int) -> int:
        rev_x = int(str(abs(x))[::-1])

        return (rev_x if x > 0 else -rev_x) if rev_x.bit_length() < 32 else 0


if __name__ == "__main__":
    x = 1534236469
    output = 0
    answer = Solution().reverse(x)
    print(answer == output, answer)
