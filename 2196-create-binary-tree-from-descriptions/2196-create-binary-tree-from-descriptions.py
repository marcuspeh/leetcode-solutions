# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hasNoParent = set()
        nodes = {}

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(val=parent)
                hasNoParent.add(parent)
            parentNode = nodes[parent]

            if child not in nodes:
                nodes[child] = TreeNode(val=child)
            childNode = nodes[child]

            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            if child in hasNoParent:
                hasNoParent.remove(child)

        if len(hasNoParent) == 0:
            return None

        root = hasNoParent.pop()
        return nodes[root]
