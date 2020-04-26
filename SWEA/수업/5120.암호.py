import sys
sys.stdin = open('5120.암호.txt')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data=d
        self.prev=p
        self.next=n

class LinkedList:
    def __init__(self):
        self.head=None
        #self.tail=None
        self.size=0

def addLast(lst, new):
    if lst.head is None:
        lst.head=new
        new.prev=new.next=new
    else:
        tail=lst.head.prev
        new.prev=tail
        new.next=lst.head
        tail.next=new
        lst.head.prev=new

    lst.size+=1


def result_append(lst):
    global result
    if lst.head is None:
        return

    cur=lst.head.prev
    if lst.size >= 10:
        length=10
    else:
        length=lst.size
    for _ in range(length):
        result.append(cur.data)
        cur=cur.prev

T=int(input())

for test_case in range(1, T+1):
    N, M, K=map(int, input().split())
    arr=list(map(int, input().split()))
    result=[]

    mylist=LinkedList()

    for val in arr:
        addLast(mylist, Node(val))

    cur=mylist.head
    for _ in range(K):
        for _ in range(M):
            cur=cur.next
        prev=cur.prev
        new=Node(prev.data+cur.data, prev, cur)
        prev.next=new
        cur.prev=new
        cur=new
        mylist.size+=1

    result_append(mylist)

    print(f'#{test_case}', end=' ')
    print(*result)