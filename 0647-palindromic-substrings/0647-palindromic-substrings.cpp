class Solution {
public:
    int countSubstrings(string s) {
        int result = s.size();
        
        for (int i = 0; i < s.size(); i++) {
            // Odd length
            int start = i;
            int end = i;
            while (start > 0 && end < s.size() - 1 && s[start - 1] == s[end + 1]) {
                start--;
                end++;
                result++;
            }
            
            // even length
            if (i == 0 || s[i - 1] != s[i]) {
                continue;
            }
            result++;
            start = i - 1;
            end = i;
            while (start > 0 && end < s.size() - 1 && s[start - 1] == s[end + 1]) {
                start--;
                end++;
                result++;
            }
        }
        return result;
    }
};