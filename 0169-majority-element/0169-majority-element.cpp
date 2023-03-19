class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int result = nums[0];
        auto numsIter = nums.begin();
        numsIter++;
        
        while (numsIter != nums.end()) {
            if (count == 0) {
                result = *numsIter;
            }
            
            count += *numsIter == result ? 1 : -1;
            numsIter++;
        }
        
        return result;
    }
};