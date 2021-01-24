# 풀이 1. 우선순위 큐를 이용한 리스트 병합

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists));
    if lists[i]:
        heapq.heappush(heap, (lists[i].val, i, lists[i]))

    
    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(neap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (reslut.next.val, idx, result.next))
        
    return root.next