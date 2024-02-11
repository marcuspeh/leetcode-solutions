class Solution {    
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int dp[70][70][70];
        memset(dp, -1, sizeof(dp));
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1];

        int ans = 0;
        for(int row = 1; row < m; row++) {
            for(int c1 = 0; c1 < n; c1++) { 
                for(int c2 = c1 + 1; c2 < n; c2++) { 
                    int highest = INT_MIN;
                    for(int x = -1; x <= 1; x++) { 
                        for(int y = -1; y <= 1; y++) {
                            int prevC1 = c1 + x;
                            int prevC2 = c2 + y;
                            if (prevC1 < 0 || prevC1 >= n) {
                                continue;
                            }
                            if (prevC2 < 0 || prevC2 >= n) {
                                continue;
                            }
                            int prev = dp[row-1][prevC1][prevC2];
                            if(prev != -1) {
                               highest = max(highest, dp[row-1][prevC1][prevC2]);
                            }
                        }
                    }
                    highest += grid[row][c1] + grid[row][c2];
                    dp[row][c1][c2] = highest;
                    ans = max(ans, highest);
                }
            }
        }
        
        return ans;
    }
};
