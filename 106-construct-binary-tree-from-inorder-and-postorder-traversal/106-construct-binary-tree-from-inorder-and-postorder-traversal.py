# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
            
        def helper(postorder, left, right):
            if not postorder or left > right:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            indexInorder = index[val]
            
            node.right = helper(postorder, indexInorder + 1, right)
            node.left = helper(postorder, left, indexInorder - 1)
            
            return node
        return helper(postorder, 0, len(postorder) - 1)
            