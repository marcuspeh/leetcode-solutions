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
    int findBottomLeftValue(TreeNode* root) {
        vector<TreeNode*> frontier;
        frontier.push_back(root);
        
        while (!frontier.empty()) {
            vector<TreeNode*> newFrontier;
            for (auto node: frontier) {
                if (node->left != nullptr) {
                    newFrontier.push_back(node->left);
                }
                if (node->right != nullptr) {
                    newFrontier.push_back(node->right);
                }
            }
            
            if (newFrontier.empty()) {
                return frontier[0]->val;
            }
            swap(newFrontier, frontier);
        }
        return -1;
    }
};