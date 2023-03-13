class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> cache;
        auto numsIter = nums.begin();
        
        for (int i = 0; i < nums.size(); i++) {
            int other = target - *numsIter;
            if (cache.count(other)) {
                return {cache[other], i};
            }
            cache.insert({*numsIter, i});
            numsIter++;
        }
        
        return {-1, -1};
    }
};