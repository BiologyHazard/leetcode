from typing import List
from collections import namedtuple
from heapq import nlargest

# class TreeNode:
#     def __init__(self):
#         pass

'''
class _Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        def search_longest_path(x):
            nonlocal longest_paths
            if longest_paths[x] != 0:
                return longest_paths[x]

            node = tree_node_list[x]
            if not node.children:
                return 1

            # longest_paths = []
            # for child_idx in node.children:
            #     child_node = tree_node_list[child_idx]
            #     if node.value == child_node.value:
            #         longest_paths.append(0)
            #     else:
            #         longest_paths.append(search_longest_path(child_node.idx))
            # if len(longest_paths) == 1:
            #     return longest_paths[0] + 1
            # return sum(sorted(longest_paths)[-2:]) + 1
            longest_path = 0
            for child_idx in node.children:
                child_node = tree_node_list[child_idx]
                if node.value == child_node.value:
                    longest_path = max(longest_path, 1)
                else:
                    longest_path = max(
                        longest_path, search_longest_path(child_node.idx) + 1)
            longest_paths[x] = longest_path
            return longest_path

        TreeNode = namedtuple(
            'TreeNode', ['idx', 'value', 'parent', 'children'])
        n = len(parents)
        tree_node_list = []
        for i in range(n):
            tree_node_list.append(TreeNode(i, s[i], parents[i], []))
        for i in range(n):
            node = tree_node_list[i]
            if node.parent != -1:
                tree_node_list[node.parent].children.append(i)

        longest_paths = [0 for i in range(n)]
        ans = 0
        for i in range(n):
            node = tree_node_list[i]
            paths = []
            for child_idx in node.children:
                child_node = tree_node_list[child_idx]
                if node.value == child_node.value:
                    paths.append(0)
                else:
                    paths.append(search_longest_path(child_idx))
            m = sum(sorted(paths)[-2:]) + 1
            ans = max(ans, m)
        return ans
'''


class _Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        def dfs(x):
            # nonlocal longest_paths, longest_paths_from_node
            node = nodes[x]
            for child_idx in node.children:
                dfs(child_idx)

            longest_path = 1  # or -inf
            for child_idx in node.children:
                child_node = nodes[child_idx]
                if node.value == child_node.value:
                    pass
                else:
                    assert longest_paths[child_idx] != 0
                    longest_path = max(
                        longest_path, longest_paths[child_idx] + 1)
            longest_paths[x] = longest_path

            longest_path_from_children = []
            for child_idx in node.children:
                child_node = nodes[child_idx]
                if node.value == child_node.value:
                    longest_path_from_children.append(0)
                else:
                    assert longest_paths[child_idx] != 0
                    longest_path_from_children.append(longest_paths[child_idx])
            longest_paths_from_node[x] = sum(
                nlargest(2, longest_path_from_children)) + 1

        TreeNode = namedtuple(
            'TreeNode', ['idx', 'value', 'parent', 'children'])

        n = len(parents)
        nodes = []
        for i in range(n):
            nodes.append(TreeNode(i, s[i], parents[i], []))
        for i in range(n):
            node = nodes[i]
            if node.parent != -1:
                nodes[node.parent].children.append(i)
            else:
                root = i  # root = 0

        longest_paths = [0 for _ in range(n)]
        longest_paths_from_node = [0 for _ in range(n)]

        dfs(root)

        return max(longest_paths_from_node)


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        ans = 0

        def dfs(x: int) -> int:
            nonlocal ans
            max_len = 0
            for child in children[x]:
                len = dfs(child) + 1
                if s[child] != s[x]:
                    ans = max(ans, max_len + len)
                    max_len = max(max_len, len)
            return max_len
        dfs(0)
        return ans + 1


if __name__ == '__main__':
    print(Solution().longestPath([-1, 137, 65, 60, 73, 138, 81, 17, 45, 163, 145, 99, 29, 162, 19, 20, 132, 132, 13, 60, 21, 18, 155, 65, 13, 163, 125, 102, 96, 60, 50, 101, 100, 86, 162, 42, 162, 94, 21, 56, 45, 56, 13, 23, 101, 76, 57, 89, 4, 161, 16, 139, 29, 60, 44, 127, 19, 68, 71, 55, 13, 36, 148, 129, 75, 41, 107, 91, 52, 42, 93, 85, 125, 89, 132, 13, 141, 21, 152, 21, 79, 160, 130, 103, 46, 65, 71, 33, 129, 0, 19, 148, 65, 125, 41, 38, 104, 115, 130, 164, 138, 108, 65, 31, 13, 60, 29, 116, 26, 58, 118, 10, 138, 14, 28, 91, 60, 47, 2, 149, 99, 28, 154, 71, 96, 60, 106, 79, 129, 83, 42, 102, 34, 41, 55, 31, 154, 26, 34, 127, 42, 133, 113, 125, 113, 13, 54, 132, 13, 56, 13, 42, 102, 135, 130, 75, 25, 80, 159, 39, 29, 41, 89, 85, 19],
                                 "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"))
