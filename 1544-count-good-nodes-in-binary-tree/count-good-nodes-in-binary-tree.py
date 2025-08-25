# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,m):
            if not node:
                return 0
            x=node.val>=m
            if x:
                c=1
            else:
                c=0
            m=max(m,node.val)
            c+=dfs(node.left,m)
            c+=dfs(node.right,m)
            return c
        return dfs(root,root.val)

        