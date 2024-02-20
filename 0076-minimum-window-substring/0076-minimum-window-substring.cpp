class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> counter;
        for (auto character: t) {
            counter[character]++;
        }
        
        int total = t.size();
        string result = "";
        int start = 0;
        for (int end = 0; end < s.size(); end++) {
            char endChar = s[end];
            if (counter.count(endChar) > 0) {
                if (counter[endChar] > 0) {
                    total--;  
                }
                counter[endChar]--;
            }
            
            if (total > 0) {
                continue;
            }
                        
            while (start < end) {
                if (counter.count(s[start]) == 0) {
                    start++;
                    continue;
                }
                if (counter[s[start]] < 0) {
                    counter[s[start]]++;
                    start++;
                    continue;
                }
                break;
            }

            if (result == "" || end - start + 1 < result.size()) {
                result = s.substr(start, end - start + 1);
            }
            
            counter[s[start]]++;
            if (counter[s[start]] > 0) {
                total++; 
            }
            start++;
        }

        return result;
    }
};