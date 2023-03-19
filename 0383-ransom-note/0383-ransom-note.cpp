class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> cache;
        
        for (char letter: magazine) {
            if (cache.count(letter)) {
                cache[letter]++;
            } else {
                cache[letter] = 1;
            }
        }
        
        for (char letter: ransomNote) {
            if (cache.count(letter) == 0 || cache[letter] <= 0) {
                return false;
            }
            
            cache[letter]--;
        }
        
        return true;
    }
};