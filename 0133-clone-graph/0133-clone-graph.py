"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        newNodes = {}
        
        def helper(node):
            nonlocal newNodes
            
            if not node:
                return None
            
            if node.val in newNodes:
                return newNodes[node.val]
            
            newNode = Node(val = node.val)
            newNodes[node.val] = newNode
            
            for neighbor in node.neighbors:
                newNode.neighbors.append(helper(neighbor))
            
            return newNode
                
        return helper(node)