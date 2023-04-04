class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> curr;
        helper(result, curr, nums);
        return result;
    }
    
    void helper(vector<vector<int>> &result, vector<int> curr, vector<int> nums) {
        if (nums.empty()) {
            result.push_back(curr);
            return;
        }
        
        int temp = nums[0];
        vector<int> newNums;
        for (int i = 1; i < nums.size(); i++) newNums.push_back(nums[i]);
        
        helper(result, curr, newNums);
        
        vector<int> newCurr = curr;
        newCurr.push_back(temp);
        helper(result, newCurr, newNums);
    }
};