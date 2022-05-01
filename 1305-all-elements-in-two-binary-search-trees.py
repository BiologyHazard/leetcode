# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root):
            def dfs(root):
                nonlocal a
                if root is None:
                    return
                dfs(root.left)
                a.append(root.val)
                dfs(root.right)
            a = []
            dfs(root)
            return a

        def merge(a1, a2):
            ans = []
            i = j = 0
            while i < len(a1) and j < len(a2):
                if a1[i] < a2[j]:
                    ans.append(a1[i])
                    i += 1
                else:
                    ans.append(a2[j])
                    j += 1
            if i < len(a1):
                ans += a1[i:]
            if j < len(a2):
                ans += a2[j:]
            return ans

        a1 = inorder(root1)
        a2 = inorder(root2)
        return merge(a1, a2)
