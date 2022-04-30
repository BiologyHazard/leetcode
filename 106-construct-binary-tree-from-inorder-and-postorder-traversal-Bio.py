<<<<<<< HEAD
# Definition for a binary tree node.

from typing import List


=======
from typing import List


# Definition for a binary tree node.
>>>>>>> fb3dd3d78381809f4fab04dda012919efae70c79
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
<<<<<<< HEAD
        def buildSub(inorder: List[int], postorder: List[int]) -> TreeNode:
            headPos = inorder.index(postorder[-1])
            a, b = None, None
            if headPos > 0:
                a = buildSub(inorder[:headPos], postorder[:headPos])
            if headPos <= len(inorder)-2:
                b = buildSub(inorder[headPos + 1:], postorder[headPos:-1])
            return TreeNode(postorder[-1], a, b)

        return buildSub(inorder, postorder)
=======
        def build(f1, f2):
            if not f1:
                return

            root_idx = f1.index(f2[-1])

            return TreeNode(f2[-1],
                            build(f1[:root_idx], f2[:root_idx]),
                            build(f1[root_idx+1:], f2[root_idx:-1]))

        return build(inorder, postorder)
>>>>>>> fb3dd3d78381809f4fab04dda012919efae70c79
