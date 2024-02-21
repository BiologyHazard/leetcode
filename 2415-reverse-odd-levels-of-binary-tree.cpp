#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode *reverseOddLevels(TreeNode *root) {
        reverse(root->left, root->right, true);
        return root;
    }
    void reverse(TreeNode *node0, TreeNode *node1, bool odd) {
        if (node1 == nullptr) return;
        // if (!root->left || !root->right) return;

        if (odd) {
            std::swap(node0->val, node1->val);
        }
        reverse(node0->left, node1->right, !odd);
        reverse(node0->right, node1->left, !odd);
    }
};
