# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def mirror(node):
            if node is None:
                return None
            return TreeNode(node.val, mirror(node.right), mirror(node.left))
        return mirror(root)
