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
        
        result = []
        frontier = [root]
        
        while frontier:
            newFrontier = []
            toAppend = []
            
            for n in frontier:
                toAppend.append(n.val)
                if n.children:
                    newFrontier.extend(n.children)
            
            result.append(toAppend)
            frontier = newFrontier
            
        return result