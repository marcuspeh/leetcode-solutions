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
        frontier1 = [root]
        frontier2 = []
        
        while frontier1 or frontier2:
            toAppend = []
            
            while frontier1:
                temp = frontier1.pop()
                toAppend.append(temp.val)
                if temp.left:
                    frontier2.append(temp.left)
                if temp.right:
                    frontier2.append(temp.right)
                    
            if toAppend:
                result.append(toAppend)
                continue
                
            while frontier2:
                temp = frontier2.pop()
                toAppend.append(temp.val)
                if temp.right:
                    frontier1.append(temp.right)
                if temp.left:
                    frontier1.append(temp.left)
            
            if toAppend:
                result.append(toAppend)
                continue
            
        return result