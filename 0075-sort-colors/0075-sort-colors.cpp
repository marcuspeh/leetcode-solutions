class Solution {
public:
    void sortColors(vector<int>& nums) {
        int redLast = 0;
        int whiteLast = 0;
        int blueFirst = nums.size() - 1;

        while (whiteLast <= blueFirst) {
            if (nums[whiteLast] == 0) {
                swap(nums[whiteLast++], nums[redLast++]);
                continue;
            } 

            if (nums[whiteLast] == 1) {
                whiteLast++;
                continue;
            }

            swap(nums[whiteLast], nums[blueFirst--]);
        }
    }
};