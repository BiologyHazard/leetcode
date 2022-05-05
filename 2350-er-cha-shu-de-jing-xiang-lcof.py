# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        # def p(self):
        #     if self.left is None and self.right is None:
        #         return f'({self.val})'
        #     if self.left is None:
        #         l = 'None'
        #     else:
        #         l = p(self.left)
        #     if self.right is None:
        #         r = 'None'
        #     else:
        #         r = p(self.right)
        #     return f'({self.val}, {l}, {r})'
        # if root:
        #     print(p(root))

        def mirror(node):
            if node is None:
                return None
            return TreeNode(node.val, mirror(node.right), mirror(node.left))
        return mirror(root)
