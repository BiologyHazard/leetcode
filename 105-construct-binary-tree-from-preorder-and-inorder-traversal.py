from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(f1, f2):
            if not f1:
                return

            root_idx = f2.index(f1[0])

            return TreeNode(f1[0],
                            build(f1[1:root_idx+1], f2[:root_idx]),
                            build(f1[root_idx+1:], f2[root_idx+1:]))

        return build(preorder, inorder)
