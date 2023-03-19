class Solution {
public:
    int longestPalindrome(string s) {
        unordered_set<char> cache;
        int pairs = 0;
        
        for (char letter: s) {
            if (cache.count(letter)) {
                pairs++;
                cache.erase(letter);
            } else {
                cache.insert(letter);
            }
        }
        
        int result = pairs * 2;
        if (cache.size()) result++;
        
        return result;
    }
};