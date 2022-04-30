# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def buildSub(inorder: List[int], postorder: List[int]) -> TreeNode:
            headPos = inorder.index(postorder[-1])
            a, b = None, None
            if headPos > 0:
                a = buildSub(inorder[:headPos], postorder[:headPos])
            if headPos <= len(inorder)-2:
                b = buildSub(inorder[headPos + 1:], postorder[headPos:-1])
            return TreeNode(postorder[-1], a, b)

        return buildSub(inorder, postorder)
