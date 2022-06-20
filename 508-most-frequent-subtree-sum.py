from collections import Counter
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                d[root.val] += 1
                return root.val
            s = dfs(root.left) + root.val + dfs(root.right)
            d[s] += 1
            return s

        d = Counter()
        dfs(root)
        c = max(d.values())
        ans = []
        for k, v in d.items():
            if v == c:
                ans.append(k)
        return ans
