def solution(enroll, referral, seller, amount):
    class Node:
        def __init__(self, name, money=0, parent=None):
            self.name = name
            self.money = money
            self.parent = parent
            
    tree = {'-': Node(name='-')}
    for enr, ref in zip(enroll, referral):
        tree[enr] = Node(name=enr, parent=ref)
        
    for curr, amnt in zip(seller, amount):
        revenue = amnt * 100
        while tree[curr].parent is not None:
            reward = int(revenue * 0.1)
            tree[curr].money += revenue - reward
            revenue = reward
            curr = tree[curr].parent
    
    del tree['-']
    return [tree[key].money for key in tree]
        

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
