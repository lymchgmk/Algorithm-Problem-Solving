import functools


def solution(sales, links):

    @functools.lru_cache(maxsize=None)
    def min_sales(node, should_include_root):
        children_sum = sum(min_sales(c, False) for c in children[node])
        sales_including_root = sales[node] + children_sum
        if should_include_root:
            return sales_including_root
        sales_without_root = children_sum + min(
            (min_sales(c, True) - min_sales(c, False) for c in children[node]),
            default=0)
        return min(sales_including_root, sales_without_root)

    children = [[] for _ in sales]
    for a, b in links:
        children[a - 1].append(b - 1)
    return min(min_sales(0, True), min_sales(0, False))


def solution(sales, links):
    def traversal(node):
        DP[node][0], DP[node][1] = 0, sales[node]

        if not salesman[node]:
            return

        extra_cost = float('inf')
        for child in salesman[node]:
            traversal(child)
            if DP[child][0] < DP[child][1]:
                DP[node][0] += DP[child][0]
                DP[node][1] += DP[child][0]
                extra_cost = min(extra_cost, DP[child][1] - DP[child][0])
            else:
                DP[node][0] += DP[child][1]
                DP[node][1] += DP[child][1]
                extra_cost = 0
        DP[node][0] += extra_cost

    N = len(sales)
    sales = {idx: sale for idx, sale in enumerate(sales, start=1)}
    salesman = {i: [] for i in range(1, N+1)}
    for parent, child in links:
        salesman[parent].append(child)

    DP = {i: [0, 0] for i in range(1, N+1)}
    traversal(1)
    return min(DP[1])


if __name__ == "__main__":
    sales = [5, 6, 5, 3, 4]
    links = [[2,3], [1,4], [2,5], [1,2]]
    print(solution(sales, links)) # 6