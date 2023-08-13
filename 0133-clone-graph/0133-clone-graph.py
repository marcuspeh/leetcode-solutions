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
            return node
        
        cache = {}
        root = Node(node.val)
        cache[node] = root
        frontier = [node]
        
        while frontier:
            node = frontier.pop()
            newNode = cache[node]
            
            for neighbor in node.neighbors:
                if neighbor in cache:
                    newNode.neighbors.append(cache[neighbor])
                    continue
                    
                newNeighbor = Node(neighbor.val)
                cache[neighbor] = newNeighbor
                newNode.neighbors.append(cache[neighbor])
                frontier.append(neighbor)
                
                
        return root
                    
            
        
        