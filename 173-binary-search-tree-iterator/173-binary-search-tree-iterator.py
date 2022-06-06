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
        node = self.stack.pop()
        
        while node.left:
            self.stack.append(node)
            temp = node
            node = node.left
            temp.left = None
        
        if node.right:
            self.stack.append(node.right)
            
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()