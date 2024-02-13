class Solution {    
    int curr[100];
public:
    int uniquePaths(int m, int n) {
        fill(&curr[0], &curr[100], 1);
    
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                curr[j] += curr[j - 1];
            }
        }
        return curr[n - 1];
    }
};