n = 5
edges = [[1,5],[2,5],[3,5],[4,5]]

from collections import deque

def distance(n1, n2):
    pass


def my_f(a, b, c):
    dist_ab, dist_bc, dist_ca = distance(a, b), distance(b, c), distance(c, a)
    dist = [dist_ab, dist_bc, dist_ca]

    return sorted(dist)[1]

def solution(n, edges):
    adj_matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for e in edges:
        adj_matrix[e[0]][e[1]] = 1
        adj_matrix[e[1]][e[0]] = 1

print(my_f(1, 2, 3))