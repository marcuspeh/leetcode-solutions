"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        
        head = Node()
        self.clone(head, node, {})
        
        return head
        
    def clone(self, head, node, visited):
        if node in visited:
            return visited[node]
        
        head.val = node.val
        visited[node] = head
        
        for n in node.neighbors:
            head.neighbors.append(self.clone(Node(), n, visited))
            
        return head
        