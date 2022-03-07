# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        frontier = [root]

        while frontier:
            curr = frontier.pop(0)
            
            otherValue = k - curr.val
            
            if otherValue in seen:
                return True
            
            seen.add(curr.val)
            
            if curr.left:
                frontier.append(curr.left)
                
            if curr.right:
                frontier.append(curr.right)
                
        return False