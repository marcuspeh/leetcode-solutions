class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        unordered_set<int> hasTrust;
        unordered_map<int, int> trustCount;
        
        for (int i = 1; i <= n; i++) {
            hasTrust.insert(i);
        }
        
        for (auto relation: trust) {
            int a = relation[0];
            int b = relation[1];
            
            if (hasTrust.count(a)) {
                hasTrust.erase(a);
            }
            trustCount[b]++;
        }
        
        for (auto maybeJudge: hasTrust) {
            if (trustCount[maybeJudge] != n - 1) {
                continue;
            }
            return maybeJudge;
        }
        
        return -1;
    }
};