"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dictt = {None:None}
        cur = head
        while cur:
            x = Node(cur.val)
            dictt[cur] = x
            cur = cur.next
        cur = head
        while cur:
            copy = dictt[cur]
            copy.next = dictt[cur.next]
            copy.random = dictt[cur.random]
            cur = cur.next
        return dictt[head]
        

            
