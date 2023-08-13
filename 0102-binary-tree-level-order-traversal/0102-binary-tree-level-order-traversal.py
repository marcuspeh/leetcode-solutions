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
        
        result = []
        frontier = [root]
        
        while frontier:
            newFrontier = []
            currLvl = []
            
            for node in frontier:
                currLvl.append(node.val)
                
                if node.left:
                    newFrontier.append(node.left)
                if node.right:
                    newFrontier.append(node.right)
            frontier = newFrontier
            result.append(currLvl)
            
        return result