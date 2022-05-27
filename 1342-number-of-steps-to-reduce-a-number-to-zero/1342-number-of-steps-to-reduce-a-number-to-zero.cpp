class Solution {
public:
    int numberOfSteps(int num) {
        int result = 0;
        while (num) {
            if (num % 2) {
                num -= 1;
            } else {
                num /= 2;
            }
            result++;
        }
        return result;
    }
};