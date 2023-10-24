# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  []
        
        result = []
        frontier = [root]
        
        while frontier:
            newFrontier = []
            highest = float("-inf")
            
            for node in frontier:
                highest = max(highest, node.val)
                
                if node.left:
                    newFrontier.append(node.left)
                if node.right:
                    newFrontier.append(node.right)
                
            result.append(highest)
            frontier = newFrontier
        
        return result