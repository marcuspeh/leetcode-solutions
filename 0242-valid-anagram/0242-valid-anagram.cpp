class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        unordered_map<char, int> cache;
        
        for(char character: s) {
            if (cache.count(character) == 0) {
                cache[character] = 0;
            }
            cache[character]++;
        }
        
        for (char character: t) {
            if (cache.count(character) == 0) {
                return false;
            }
            
            if (cache[character] <= 0) {
                return false;
            }
            
            cache[character]--;
            if (cache[character] == 0) {
                cache.erase(character);
            }
        }        
        return cache.size() == 0;
        
    }
};