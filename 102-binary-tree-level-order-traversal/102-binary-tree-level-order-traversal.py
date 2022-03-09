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
        curr = [root]
        
        while curr:
            newCurr = []
            toAppend = []
            
            for node in curr:
                toAppend.append(node.val)
                if node.left:
                    newCurr.append(node.left)
                if node.right:
                    newCurr.append(node.right)
                    
            curr = newCurr
            result.append(toAppend)
        return result