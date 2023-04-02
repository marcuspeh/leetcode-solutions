class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0, 0, 0};
        for (auto num: nums) count[num]++;
        
        count[1] += count[0];
        count[2] += count[1];
        int temp[nums.size()];
        for (int i = nums.size() - 1; i >= 0; i--) {
            int curr = nums[i];
            
            temp[--count[curr]] = curr;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            nums[i] = temp[i];
        }
    }
};