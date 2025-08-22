from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        m=0
        q=deque()
        if root.left:
            q.append((root.left,'left',1))
        if root.right:
            q.append((root.right,'right',1))
        while q:
            node,d,len=q.popleft()
            m=max(m,len)
            if d=='left':
                if node.right:
                    q.append((node.right,'right',len+1))
                if node.left:
                    q.append((node.left,'left',1))
            else:
                if node.left:
                    q.append((node.left,'left',len+1))
                if node.right:
                    q.append((node.right,'right',1))
        return m

        