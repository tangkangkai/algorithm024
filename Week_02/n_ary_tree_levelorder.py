"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        next_queue = []
        res = []
        
        while queue:
            level = []
            for node in queue:
                level.append(node.val)
                if node.children:
                    next_queue += node.children
            res.append(level)
            queue = next_queue
            next_queue = []
        
        return res