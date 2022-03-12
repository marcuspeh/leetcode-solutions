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
        
        def helper(head):
            nonlocal cache
            
            if not head:
                return None
            
            if head in cache:
                return cache[head]
            
            newHead = Node(head.val)
            cache[head] = newHead
            
            newHead.next = helper(head.next)
            
            if head.random and head.random in cache:
                newHead.random = cache[head.random]
            else:
                newHead.random = helper(head.random)
                
            return newHead
            
        
        return helper(head)