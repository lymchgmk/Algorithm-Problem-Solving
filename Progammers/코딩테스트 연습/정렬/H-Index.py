citations = [3, 0, 6, 1, 5]

def my_solution(citations):
    for h in range(len(citations), -1, -1):
        c = len(list(filter(lambda x: x if x>=h else 0, citations)))
        if h <= c: return h;
    return 0

print(my_solution(citations))