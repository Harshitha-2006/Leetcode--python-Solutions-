"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        n=root
        while n:
            d=Node(0)
            t=d
            while n:
                if n.left:
                    t.next=n.left
                    t=t.next
                if n.right:
                    t.next=n.right
                    t=t.next
                n=n.next
            n=d.next
        return root