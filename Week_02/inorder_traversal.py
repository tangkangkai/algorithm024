# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = []
        self.push_left(stack, root)
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                self.push_left(stack, node.right)
        return res
    
    def push_left(self, stack, node):
        while node:
            stack.append(node)
            node = node.left