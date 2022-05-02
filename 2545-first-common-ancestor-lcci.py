# Definition for a binary tree node.
from turtle import right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def search(root):
        #     nonlocal ans
        #     if root is None:
        #         return False
        #     l = search(root.left)
        #     r = search(root.right)
        #     m = ((root == p) or (root == q))
        #     if (l and r) or (r and m) or (l and m):
        #         ans = root
        #         return True
        #     return l or r or m
        # ans = None
        # search(root)
        # return ans

        if root is None:
            return None
        if p == root or q == root:
            return root
        left = Solution().lowestCommonAncestor(root.left, p, q)
        right = Solution().lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        if left is None:
            return right
        return left
