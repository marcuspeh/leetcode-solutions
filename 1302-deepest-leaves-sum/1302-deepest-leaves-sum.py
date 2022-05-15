# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        frontier = [root]
        result = root.val
        
        while frontier:
            newFrontier = []
            newResult = 0
            
            for n in frontier:
                if n.left:
                    newFrontier.append(n.left)
                    
                if n.right:
                    newFrontier.append(n.right)
                
                newResult += n.val
                
            frontier = newFrontier
            result = newResult
            
        return result