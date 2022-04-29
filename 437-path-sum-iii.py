from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def search(root, target, isfather):
            count = 0
            if target == root.val:
                count += 1
            if root.left:
                count += search(root.left, target - root.val, 0)
            if root.right:
                count += search(root.right, target - root.val, 0)
            if root.left and isfather:
                count += search(root.left, targetSum, 1)
            if root.right and isfather:
                count += search(root.right, targetSum, 1)
            return count
        count = 0
        if root:
            count = search(root, targetSum, 1)
        return count
