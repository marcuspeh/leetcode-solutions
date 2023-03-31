class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        vector<vector<int>> result;
        
        sort(intervals.begin(), intervals.end(), Solution().comparator);
        
        result.push_back(intervals[0]);
        int last = intervals[0][1];
        
        for (int i = 1; i < intervals.size(); i++) {
            vector<int> curr = intervals[i];
            if (curr[0] <= last) {
                result[result.size() - 1][1] = max(last, curr[1]);
                last = max(last, curr[1]);
            } else {
                result.push_back(curr);
                last = curr[1];
            }
        }
        return result;                                 
                                   
            
    }
    
    static bool comparator(vector<int> x1, vector<int> x2) {
        return x1[0] < x2[0];
    }

};