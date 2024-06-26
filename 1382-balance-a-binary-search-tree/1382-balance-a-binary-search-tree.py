# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.getInorder(root, inorder)
        return self.buildTree(inorder, 0, len(inorder) - 1)
        
    def getInorder(self, root, result):
        if not root:
            return
        
        self.getInorder(root.left, result)
        result.append(root.val)
        self.getInorder(root.right, result)
    
    def buildTree(self, inorder, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(inorder[left])
        
        mid = (right + left) // 2
        node = TreeNode(inorder[mid])
        node.left = self.buildTree(inorder, left, mid - 1)
        node.right = self.buildTree(inorder, mid + 1, right)
        return node