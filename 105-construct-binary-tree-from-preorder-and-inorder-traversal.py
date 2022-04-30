# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildSub(preorder: List[int], inorder: List[int]) -> TreeNode:
            headPos = inorder.index(preorder[0])
            a, b = None, None
            if headPos > 0:
                a = buildSub(preorder[1:headPos+1], inorder[:headPos])
            if headPos <= len(inorder)-2:
                b = buildSub(preorder[headPos+1:], inorder[headPos+1:])
            return TreeNode(preorder[0], a, b)

        return buildSub(preorder, inorder)
