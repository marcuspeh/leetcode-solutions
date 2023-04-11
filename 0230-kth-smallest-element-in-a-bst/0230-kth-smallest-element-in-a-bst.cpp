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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode *> frontier;
        frontier.push(root);
        int visited = 0;
        
        while (!frontier.empty()) {
            TreeNode* node = frontier.top();
            frontier.pop();
            
            while (node->left != nullptr) {
                TreeNode* temp = node->left;
                node->left = nullptr;
                frontier.push(node);
                node = temp;
            }
            
            visited++;
            if (visited == k) return node->val;
            
            if (node->right != nullptr) frontier.push(node->right);
        }
        
        return -1;
    }
};