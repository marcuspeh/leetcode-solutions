class Solution {    
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(n, -1)));
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1];

        int ans = 0;
        for(int row = 1; row < m; row++) {
            for(int j = 0; j < n; j++) { 
                for(int k = j+1; k < n; k++) { 
                    int highest = INT_MIN;
                    for(int x = -1; x <= 1; x++) { 
                        for(int y = -1; y <= 1; y++) {
                            int nj = j + x;
                            int nk = k + y;
                            if(nj >= 0 && nj < n && nk >= 0 && nk < n) {
                                int prev = dp[row-1][nj][nk];
                                if(prev != -1) {
                                   highest = max(highest, prev + grid[row][j] + (j != k ? grid[row][k] : 0));
                                }
                            }
                        }
                    }
                    dp[row][j][k] = highest;
                    ans = max(ans, highest);
                }
            }
        }
        
        return ans;
    }
};
