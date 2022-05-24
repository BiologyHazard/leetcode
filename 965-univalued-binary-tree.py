# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: 'TreeNode' | None = None, right: 'TreeNode' | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode | None) -> bool:
            if root is None:
                return True
            if root.val != value:
                return False
            return dfs(root.left) and dfs(root.right)
        value = root.val
        return dfs(root)
