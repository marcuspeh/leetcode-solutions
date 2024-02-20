class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int longest = 0;
        int result = 0;
        
        for (int i = 0; i < s.size(); i++) {
            count[s[i]]++;
            longest = max(longest, count[s[i]]);
            if (result - longest < k) {
                result++;
                continue;
            }
            count[s[i - result]] -= 1;
        }
        return result;
    }
};
