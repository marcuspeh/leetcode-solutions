/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> index;
        for (int i = 0; i < inorder.size(); i++) index[inorder[i]] = i;

        return helper(preorder, index, 0, preorder.size() - 1);
    }
    
    TreeNode* helper(vector<int>& preorder, unordered_map<int, int>& index, int left, int right) {
        if (preorder.empty() || left > right) {
            return nullptr;
        }

        int val = preorder[0];
        TreeNode *node = new TreeNode(val);
        preorder.erase(preorder.begin());

        int indexInOrder = index[val];

        node->left = helper(preorder, index, left, indexInOrder - 1);
        node->right = helper(preorder, index, indexInOrder + 1, right);

        return node;
    }
};
    