class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Find smallest element
        int start = 0;
        int end = nums.size() - 1;
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            
            if (nums[mid] < nums[end]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        int offset = start;
        
        start = 0;
        end = nums.size() - 1;
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            int trueMid = getTrueIndex(mid, offset, nums.size());
            
            if (nums[trueMid] < target) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        
        start = getTrueIndex(start, offset, nums.size());
        return nums[start] == target ? start : -1;
    }
    
    int getTrueIndex(int initial, int add, int total) {
        return (initial + add) % total;
    }
};