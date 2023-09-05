"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        
        def helper(node):
            nonlocal cache
            
            if not node:
                return
            
            if node in cache:
                return cache[node]
            
            newNode = Node(node.val)
            cache[node] = newNode
            newNode.next= helper(node.next)
            newNode.random = helper(node.random)
            
            return newNode
        return helper(head)
                