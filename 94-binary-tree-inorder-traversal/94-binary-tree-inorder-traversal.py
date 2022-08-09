# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root:
            return result
        
        stack = [root]
        
        while stack:
            node = stack.pop()

            while node.left:
                temp = node.left
                node.left = None
                stack.append(node)
                node = temp

            result.append(node.val)
            if node.right:
                stack.append(node.right)
        return result