# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        def inorder(root):
            nonlocal flag
            if root is None:
                return None

            l = inorder(root.left)
            if flag:
                flag = False
                return root
            if root == p:
                flag = True
            r = inorder(root.right)

            if l is not None:
                return l
            return r

        flag = False
        return inorder(root)
