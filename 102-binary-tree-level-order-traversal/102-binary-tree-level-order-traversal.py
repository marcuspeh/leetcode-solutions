# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = [[root.val]]
        frontier = [root]
        
        while frontier:
            newFrontier = []
            newResult = []
            
            for node in frontier:
                if node.left:
                    newFrontier.append(node.left)
                    newResult.append(node.left.val)
                    
                if node.right:
                    newFrontier.append(node.right)
                    newResult.append(node.right.val)
                    
            if newResult:
                result.append(newResult)
            frontier = newFrontier
            
        return result