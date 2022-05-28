class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0;
        int end = numbers.size() - 1;
        
        while (start < end) {
            int total = numbers.at(start) + numbers.at(end);
            
            if (total == target) {
                return {start + 1, end + 1};
            } else if (total < target) {
                start ++;
            } else {
                end--;
            }
        }
        return {-1, -1};
    }
};