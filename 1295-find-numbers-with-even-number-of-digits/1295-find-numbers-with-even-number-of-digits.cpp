class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int result = 0;
        for (auto num: nums) {
            if (evenNumber(num) % 2 == 0) {
                result++;
            }
        }

        return result;
    }

    int evenNumber(int num) {
        int result = 0;
        while (num > 0) {
            result++;
            num /= 10;
        }

        return result;
    }
};