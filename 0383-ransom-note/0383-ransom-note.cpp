class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> cache;
        
        for (char letter: magazine) {
            cache[letter]++;
        }
        
        for (char letter: ransomNote) {
            if (--cache[letter] < 0) {
                return false;
            }
        }
        
        return true;
    }
};