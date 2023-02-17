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
    int minDiffInBST(TreeNode* root) {
        if (root == nullptr) return -1;
        
        int result = 100001;
        int prev = -100000;
        vector<TreeNode *> stack = {root};
        while (!stack.empty()) {
            TreeNode *nextNode = stack.back();
            stack.pop_back();
            
            while (nextNode->left) {
                TreeNode *tempNode = nextNode->left;
                nextNode->left = nullptr;
                stack.push_back(nextNode);
                nextNode = tempNode;
            }
            
            result = min(result, nextNode->val - prev);
            prev = nextNode-> val;
            
            if (nextNode->right) stack.push_back(nextNode->right);
        }
        
        return result;
    }
};