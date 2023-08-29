class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr_penalty = min_penalty = customers.count('Y')
        best_hour = 0

        for hour, customer in enumerate(customers, start=1):
            curr_penalty += -1 if customer == 'Y' else 1

            if curr_penalty < min_penalty:
                best_hour = hour
                min_penalty = curr_penalty

        return best_hour


if __name__ == "__main__":
    solution = Solution()
    customers = "NNNNN"
    print(solution.bestClosingTime(customers=customers))
