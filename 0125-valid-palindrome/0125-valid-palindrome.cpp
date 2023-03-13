class Solution {
public:
    bool isPalindrome(string s) {
        auto start = s.begin();
        auto end = s.end();
        
        while (start < end) {
            while (start < end && !iswalnum(*start)) {
                start++;
            }
            
            while (start < end && !iswalnum(*end)) {
                end--;
            }
            
            if (tolower(*start) != tolower(*end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};