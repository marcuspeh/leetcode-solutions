/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) {
            return nullptr;
        }
        
        TreeNode* smaller = p->val < q->val ? p : q;
        TreeNode* larger = p->val < q->val ? q : p;
        
        if (smaller->val <= root->val && root->val <= larger->val) {
            return root;
        }
        
        if (larger->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        if (smaller->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        return nullptr;
    }
};