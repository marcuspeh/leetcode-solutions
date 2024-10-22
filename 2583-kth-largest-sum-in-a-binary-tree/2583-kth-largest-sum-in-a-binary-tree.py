
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        heap = []
        stack = [root]
        while stack:
            newStack = []
            count = 0
            for node in stack:
                count += node.val
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            stack = newStack
            heapq.heappush(heap, count)
            if len(heap) > k:
                heapq.heappop(heap)
        
        if len(heap) != k:
            return -1
        return heap[0]