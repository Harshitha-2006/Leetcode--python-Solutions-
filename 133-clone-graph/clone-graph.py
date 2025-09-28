"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        v={}
        def dfs(curr_node):
            if curr_node in v:
                return v[curr_node]
            c=Node(curr_node.val)
            v[curr_node]=c
            for i in curr_node.neighbors:
                c.neighbors.append(dfs(i))
            return c
        return dfs(node)
        