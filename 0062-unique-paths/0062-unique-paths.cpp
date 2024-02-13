class Solution {
    int curr[101];
    
public:
    int uniquePaths(int m, int n) {
        // memset(curr, 1, sizeof(curr));
        vector<int> curr(n, 1);
    
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                curr[j] += curr[j - 1];
            }
        }
        return curr[n - 1];
    }
};