# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(preorder, inorder, left, right):
        
            if not preorder or right < left:
                return None

            root = TreeNode(preorder.pop(0))

            index = inorder.index(root.val)

            root.left = helper(preorder, inorder, left, index - 1)
            root.right = helper(preorder, inorder, index + 1, right)

            return root
        return helper(preorder, inorder, 0, len(inorder) - 1)