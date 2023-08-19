# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        frontier = [root]
        while frontier:
            newFrontier = []
            for node in frontier:
                if node.left:
                    newFrontier.append(node.left)
                
                if node.right:
                    newFrontier.append(node.right)
            result.append(frontier[-1].val)
            frontier = newFrontier
            
        return result
        