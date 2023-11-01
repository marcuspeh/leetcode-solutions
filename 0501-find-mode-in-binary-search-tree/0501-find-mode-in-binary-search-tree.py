# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        frontier = [root]
        
        while frontier:
            node = frontier.pop()
            if node.val not in count:
                count[node.val] = 0
            count[node.val] += 1
            
            if node.left:
                frontier.append(node.left)
            
            if node.right:
                frontier.append(node.right)
        
        result = []
        maxCount = 0
        for val, n in count.items():
            if n > maxCount:
                result = [val]
                maxCount = n
            elif n == maxCount:
                result.append(val)
        
        return result
        