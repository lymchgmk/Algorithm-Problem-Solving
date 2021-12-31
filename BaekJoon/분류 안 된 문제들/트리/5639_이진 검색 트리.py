import sys
sys.stdin = open('5639_이진 검색 트리.txt', 'r')


def postorder(start, end):
    if start > end:
        return
    
    root = preordered[start]
    div = end + 1
    for i in range(start+1, end+1):
        if root < preordered[i]:
            div = i
            break
    postorder(start+1, div-1)
    postorder(div, end)
    print(root)


input = lambda: sys.stdin.readline().strip()
preordered = []
while True:
    key = input()
    if not key:
        break
    else:
        preordered.append(int(key))
postorder(0, len(preordered)-1)
