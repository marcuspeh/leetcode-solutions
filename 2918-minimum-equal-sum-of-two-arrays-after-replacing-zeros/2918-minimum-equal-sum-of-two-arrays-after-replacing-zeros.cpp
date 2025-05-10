class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long countA = 0;
        long long countB = 0;
        long long zeroA = 0;
        long long zeroB = 0;

        for (auto num: nums1) {
            countA += num;
            if (num == 0) {
                zeroA++;
                countA++;
            }
        }

        for (auto num: nums2) {
            countB += num;
            if (num == 0) {
                zeroB++;
                countB++;
            }
        }

        if (countA > countB && zeroB == 0) {
            return -1;
        }
        if (countA < countB && zeroA == 0) {
            return -1;
        }

        return max(countA, countB);
    }
};