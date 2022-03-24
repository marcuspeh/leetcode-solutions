# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]

    def next(self) -> int:
        curr = self.stack.pop()
        
        while curr.left:
            self.stack.append(curr)
            curr = curr.left
            self.stack[-1].left = None
            
        temp = curr.val
        
        if curr.right:
            self.stack.append(curr.right)
            
        return temp

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()