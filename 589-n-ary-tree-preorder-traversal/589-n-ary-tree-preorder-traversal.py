"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        def helper(root):
            nonlocal result
            
            if not root:
                return
            
            result.append(root.val)
            for c in root.children:
                helper(c)
        
        helper(root)
        
        return result