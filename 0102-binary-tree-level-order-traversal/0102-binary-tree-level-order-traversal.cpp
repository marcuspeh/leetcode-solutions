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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<vector<int>> result;
        vector<TreeNode*> frontier {root};
        
        while (!frontier.empty()) {
            vector<TreeNode*> newFrontier;
            vector<int> curr;
            
            for (auto node: frontier) {
                curr.push_back(node->val);
                if (node->left != nullptr) {
                    newFrontier.push_back(node->left);
                }
                if (node->right != nullptr) {
                    newFrontier.push_back(node->right);
                }
            }
            swap(frontier, newFrontier);
            result.push_back(curr);
        }
        return result;
    }
};