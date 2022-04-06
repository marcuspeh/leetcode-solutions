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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        frontier = [root]
        
        while frontier:
            newFrontier = []
            
            for i in range(len(frontier)):
                node = frontier[i]
                if node.left:
                    newFrontier.append(node.left)
                    
                if node.right:
                    newFrontier.append(node.right)
                    
                if i < len(frontier) - 1:
                    node.next = frontier[i + 1]
                    
            frontier = newFrontier
            
        return root

            
                    
                