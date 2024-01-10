# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        cache = {}
        parentDict  = {}
        frontier = [(root, None)]
        while frontier:
            curr, parent = frontier.pop()
            cache[curr.val] = curr
            if parent:
                parentDict[curr.val] = parent
            if curr.left:
                frontier.append((curr.left, curr.val))
            if curr.right:
                frontier.append((curr.right, curr.val))
                
        result = -1
        frontier = [start]
        visited = set()
        while frontier:
            newFrontier = []
            for curr in frontier:
                node = cache[curr]
                visited.add(curr)
                if node.left and node.left.val not in visited:
                    newFrontier.append(node.left.val)
                if node.right and node.right.val not in visited:
                    newFrontier.append(node.right.val)
                    
                if node.val not in parentDict:
                    continue
                parent = cache[parentDict[node.val]]
                if parent.val not in visited:
                    newFrontier.append(parent.val)
            frontier = newFrontier
            result += 1
        return result