from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m,l,ml=-float('inf'),0,0
        q=deque()
        q.append(root)
        while q:
            l+=1
            s=0
            for _ in range(len(q)):
                x=q.popleft()
                s+=x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            if m<s:
                m,ml=s,l
        return ml