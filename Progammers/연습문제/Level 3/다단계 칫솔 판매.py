def solution(enroll, referral, seller, amount):
    class Node:
        def __init__(self, name, money=0, parent=None):
            self.name = name
            self.money = money
            self.parent = parent
            self.children = {}
            
    tree = {'-': Node('-')}
    for enr, ref in zip(enroll, referral):
        tree[enr] = Node(name=enr, parent=ref)
        tree[ref].children[enr] = True
        
    for seller, amount in zip(seller, amount):
        revenue = amount * 100
        
        
    
    
    
    


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
