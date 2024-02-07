class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char,int> freq;
        for(char c:s) {
            freq[c]++;
        }
        
        vector<string> bucket(s.size()+1, "");
        for(auto& it:freq) {
            int n = it.second;
            char c = it.first;
            bucket[n].append(n, c);
        }
        
        string res;
        for(int i=s.size(); i>0; i--) {
            if(bucket[i].empty()) {
                continue;
            }
            res.append(bucket[i]);
        }
        return res;
    }
};