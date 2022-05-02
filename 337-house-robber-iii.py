from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def search(root: TreeNode) -> Tuple[int, int]:
            if root is None:
                return 0, 0
            l1, l2 = search(root.left)
            r1, r2 = search(root.right)
            a1 = l2 + r2 + root.val
            a2 = max(l1, l2) + max(r1, r2)
            return a1, a2
        return max(search(root))
