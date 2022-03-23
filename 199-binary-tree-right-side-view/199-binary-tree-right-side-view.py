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
            nextFrontier = []
            result.append(frontier[-1].val)
            
            for node in frontier:
                if node.left:
                    nextFrontier.append(node.left)
                if node.right:
                    nextFrontier.append(node.right)
            frontier = nextFrontier
            
        
        return result