class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result;
        result.push_back(1);
        
        for (int num: nums) {
            result.push_back(result.back() * num);
        }
        
        result.pop_back();
        int back = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] *= back;
            back *= nums[i];
        }
        
        return result;
    }
};