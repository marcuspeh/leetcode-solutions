class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int count[100];
        for (int i = 0; i < 100; i++) {
            count[i] = 0;
        }
        
        for (auto num: nums) {
            count[num - 1] += 1;
        }
        
        int result = 0;
        int highest = 0;
        for (auto c: count) {
            if (c < highest) {
                continue;
            }
            if (c > highest) {
                highest = c;
                result = 0;
            }
            result += c;
        }
        return result;
    }
};