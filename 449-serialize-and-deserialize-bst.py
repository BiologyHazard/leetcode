# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(root: TreeNode | None) -> None:
            nonlocal l
            if root is None:
                return
            l.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        l = []
        preorder(root)
        return ' '.join(l)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def construct(preorder: list[int], inorder: list[int]) -> TreeNode | None:
            if len(preorder) == 0:
                return None
            root_idx = inorder.index(preorder[0])
            return TreeNode(
                preorder[0],
                construct(preorder[1:root_idx+1], inorder[:root_idx]),
                construct(preorder[root_idx+1:], inorder[root_idx+1:]))

        preorder = list(map(int, data.split()))
        inorder = sorted(preorder)
        return construct(preorder, inorder)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
