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
            
            if isLeft:
                for i in frontier:
                    toAppend.append(i.val)
                    if i.left:
                        newFrontier.append(i.left)
                    if i.right:
                        newFrontier.append(i.right)
            else:
                for i in range(len(frontier) - 1, -1, -1):
                    node = frontier[i]
                    toAppend.append(node.val)
                    if node.right:
                        newFrontier.insert(0, node.right)
                    if node.left:
                        newFrontier.insert(0, node.left)
            
            isLeft = not isLeft
            result.append(toAppend)
            frontier = newFrontier
            
        return result