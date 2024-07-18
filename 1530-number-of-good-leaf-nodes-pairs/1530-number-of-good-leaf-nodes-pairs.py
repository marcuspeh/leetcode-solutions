# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        
        def helper(root):
            nonlocal result
            if not root:
                return {}
            if not root.left and not root.right:
                return {1: 1}
            
            leftCount = helper(root.left)
            rightCount = helper(root.right)
            for d, count in leftCount.items():
                for i in range(1, distance - d + 1):
                    if i not in rightCount:
                        continue
                    result += rightCount[i] * count
            
            newCount = {}
            for d, count in leftCount.items():
                if d >= distance:
                    continue
                if d + 1 not in newCount:
                    newCount[d + 1] = 0
                newCount[d + 1] += count
            for d, count in rightCount.items():
                if d >= distance:
                    continue
                if d + 1 not in newCount:
                    newCount[d + 1] = 0
                newCount[d + 1] += count
            return newCount
        
        helper(root)
        return result