# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        
        def helper(preorder, left, right):
            if not preorder or right < left:
                return None
            
            val = preorder.pop(0)
            node = TreeNode(val)
            
            indexInInorder = index[val]
            
            node.left = helper(preorder, left, indexInInorder - 1)
            node.right = helper(preorder, indexInInorder + 1, right)
        
            return node
        
        return helper(preorder, 0, len(preorder) - 1)