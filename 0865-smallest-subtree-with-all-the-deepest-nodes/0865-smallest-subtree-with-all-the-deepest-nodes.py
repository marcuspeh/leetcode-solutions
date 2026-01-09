# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = {}
        frontier = [root]
        lastLevel = [root]
        while frontier:
            newFrontier = []
            lastLevel = frontier
            for node in frontier:
                if node.left:
                    parent[node.left.val] = node
                    newFrontier.append(node.left)
                if node.right:
                    parent[node.right.val] = node
                    newFrontier.append(node.right)
            frontier = newFrontier
        
        while len(lastLevel) > 1:
            prevLevel = []
            seenParent = set()

            for node in lastLevel:
                currParent = parent[node.val]
                if currParent.val in seenParent:
                    continue
                seenParent.add(currParent.val)
                prevLevel.append(currParent)
            
            lastLevel = prevLevel
            
        return lastLevel[0]