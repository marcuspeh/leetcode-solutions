# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        
        index = inorder.index(root.val)
        leftInorder = inorder[:index]
        rightInorder = inorder[index + 1:]
        
        root.left = self.buildTree(preorder, leftInorder)
        root.right = self.buildTree(preorder, rightInorder)
        
        return root