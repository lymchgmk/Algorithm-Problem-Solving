import sys
sys.stdin = open('5110.수열합치기.txt')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data=d
        self.prev=p
        self.next=n

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

def addList(lst, arr):
    first=last=Node(arr[0])
    for val in arr[1:]:
        new=Node(val, last)
        last.next=new
        last=new

    if lst.head is None:
        lst.head, lst.tail=first, last

    else:
        cur=lst.head
        while cur is not None:
            if cur.data>arr[0]: break
            cur=cur.next
        if cur is None:
            first.prev=lst.tail
            lst.tail.next=first
            lst.tail=last
        elif cur.prev is None:
            last.next=lst.head
            lst.head.prev=last
            lst.head=first
        else:
            prev=cur.prev
            first.prev=prev
            last.next=cur
            prev.next=first
            cur.prev=last
    lst.size += len(arr)

def result_append(lst):
    global result
    if lst.head is None:
        return

    cur=lst.tail
    if lst.size >= 10:
        length=10
    else:
        length=lst.size
    for _ in range(length):
        result.append(cur.data)
        cur=cur.prev


T=int(input())

for test_case in range(1, T+1):
    N, M=map(int, input().split())
    arr=list(map(int, input().split()))
    result=[]

    mylist=LinkedList()
    addList(mylist, arr)
    for M_case in range(M-1):
        addList(mylist, list(map(int, input().split())))

    result_append(mylist)

    print(f'#{test_case}', end=' ')
    print(*result)


# arr=[1,3,5,7,9]
# addList(mylist, arr)
# printList(mylist)
#
# addList(mylist, [0, 1, 2])
# printList(mylist)
# addList(mylist, [4, 4, 4])
# printList(mylist)
# addList(mylist, [10, 4, 4])
# printList(mylist)
