"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(node, visited):
            if not node:
                return None
            
            if node.val in visited:
                return visited[node.val]
            
            root = Node(node.val)
            visited[node.val] = root
            
            for n in node.neighbors:
                root.neighbors.append(helper(n, visited))
                
            
            return root
    
        return helper(node, {})