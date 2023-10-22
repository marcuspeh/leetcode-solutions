# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "x"
        
        return f"{root.val} {self.serialize(root.left)} {self.serialize(root.right)}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = list(map(lambda x: int(x) if x != "x" else None, data.split(" ")))
        index = 0
        
        def helper():
            nonlocal index
            
            if values[index] == None:
                index += 1
                return None
            
            node = TreeNode(values[index])
            index += 1
            node.left = helper()
            node.right = helper()
            return node
        return helper()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))