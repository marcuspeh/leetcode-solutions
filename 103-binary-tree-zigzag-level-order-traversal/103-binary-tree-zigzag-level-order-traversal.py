# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        frontier = [root]
        isLeft = True
        
        while frontier:
            newFrontier = []
            toAppend = []
            
            for i in frontier:
                toAppend.append(i.val)
                if i.left:
                    newFrontier.append(i.left)
                if i.right:
                    newFrontier.append(i.right)

            if not isLeft: 
                result.append(toAppend[::-1])
            else:
                result.append(toAppend)
            isLeft = not isLeft
            frontier = newFrontier
            
        return result