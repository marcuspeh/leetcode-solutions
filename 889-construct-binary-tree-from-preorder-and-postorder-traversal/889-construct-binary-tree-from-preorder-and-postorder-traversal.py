# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

    
        preIndex, posIndex = 0, 0
        def helper(pre, post):
            nonlocal preIndex, posIndex
            root = TreeNode(pre[preIndex])
            preIndex += 1
            if (root.val != post[posIndex]):
                root.left = helper(pre, post)
            if (root.val != post[posIndex]):
                root.right = helper(pre, post)
            posIndex += 1
            return root
        return helper(preorder, postorder)