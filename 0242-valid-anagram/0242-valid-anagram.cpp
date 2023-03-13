class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        unordered_map<char, int> cache;
        auto sIter = s.begin();
        auto tIter = t.begin();
        
        for(int i = 0; i < s.size(); i++) {
            cache[*sIter]++;
            cache[*tIter]--;
            sIter++;
            tIter++;
        }
        
        for (auto charCount: cache) {
            if (charCount.second != 0) {
                return false;
            }
        }        
        return true;
        
    }
};