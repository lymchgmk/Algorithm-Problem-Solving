import sys
sys.stdin = open('전화번호 목록.txt')

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook[:-1], phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
#
# phoneBook = input()
#
# answer = solution(phoneBook)
#
# print(answer)

# 트라이 내에 담을 노드
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

# 트라이 구현 부분.
class Trie(object):
    def __init__(self):
        # 루트 노드는 None, 밑에서부터 하나씩 삽입!
        self.head = Node(None)

        """
        트라이에 문자열 삽입
        """

    def insert(self, string):
        curr_node = self.head
        # 루트부터 하나씩 내려가요 !! 뒤에 삽입하다 앞 요소 발견 시 False
        for char in string:
            if curr_node.data != None : return False
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 밑으로 내려감
            curr_node = curr_node.children[char]
        # string의 마지막 글자이면,
        # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다. (True 해도댐...)
        curr_node.data = string
        return True


    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                # 안에 데이터 담겨있으면 False
                if curr_node.data != None: return False
                curr_node = curr_node.children[char]

        return True



def solution(phone_book:list)->bool:
    tri = Trie()
    answer = True
    for p in phone_book:
        if not tri.insert(p) :   return False
    for p in phone_book:
        if not tri.search(p) :  return False
    return answer