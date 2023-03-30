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
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) return true;
        
        stack<TreeNode*> frontier;
        frontier.push(root);
        int last = INT_MIN;
        bool isNotIntMin = true;
        
        while (!frontier.empty()) {
            TreeNode* node = frontier.top();
            frontier.pop();
            
            while (node->left != nullptr) {
                TreeNode* temp = node->left;
                node->left = nullptr;
                frontier.push(node);
                node = temp;
            }
            
            if (node->val <= last && !isNotIntMin) return false;
            if (node->val <= last && node->val != INT_MIN) return false;
            isNotIntMin = false;
            last = node->val;
            
            if (node->right) frontier.push(node->right);
        }
        
        return true;
    }
};