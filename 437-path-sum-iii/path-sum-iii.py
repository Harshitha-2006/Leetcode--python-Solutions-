from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.c=0
        p=defaultdict(int)
        p[0]=1
        def dfs(node,curr_sum):
            if not node:
                return 
            curr_sum+=node.val
            self.c+=p[curr_sum-targetSum]
            p[curr_sum]+=1
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            p[curr_sum]-=1
        dfs(root,0)
        return self.c
        