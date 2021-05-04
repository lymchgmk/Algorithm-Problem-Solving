class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        
        
class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            curr_node = curr_node.children[char]
        
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        if curr_node.data is not None:
            return True
    
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return None
            
        queue = list(subtrie.children.values())
        while queue:
            curr = queue.pop()
            if curr.data is not None:
                result.append(curr.data)
            
            queue += list(curr.children.values())
        
        return result
