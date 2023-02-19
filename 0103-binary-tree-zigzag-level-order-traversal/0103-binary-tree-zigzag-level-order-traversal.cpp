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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) {
            return {};
        }
        bool isReversed = false;
        
        vector<vector<int>> result;
        vector<TreeNode* > frontier = {root};
        
        while (!frontier.empty()) {
            vector<TreeNode*> newFrontier;
            vector<int> currLvl;
            
            for (TreeNode* node: frontier) {
                currLvl.push_back(node->val);
                if (node->left) newFrontier.push_back(node->left);
                if (node->right) newFrontier.push_back(node->right);
            }
            
            frontier = newFrontier;
            
            if (isReversed) {
                reverse(currLvl.begin(), currLvl.end());
            }
            isReversed = !isReversed;
            result.push_back(currLvl);
        }
        
        return result;
    }
};