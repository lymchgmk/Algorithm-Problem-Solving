import heapq


def solution(operations):
    answer = []
    heap = []
    heapq.heapify(heap)
    for op in operations:
        char, num = op.split()
        num = int(num)
        if char == 'I':
            heapq.heappush(heap, num)
        else:
            if heap:
                if num == 1:
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                elif num == -1:
                    heapq.heappop(heap)
    
    if not heap:
        return [0, 0]
    else:
        return [heapq.nlargest(1, heap)[0], heap[0]]


operations = ["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]
print(solution(operations))