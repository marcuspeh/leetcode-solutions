class Solution {    
    int prevLayer[70][70];
    int currLayer[70][70];
    
    void moveLayer() {
        for (int i = 0; i < 70; i++) {
            for (int j = 0; j < 70; j++) {
                prevLayer[i][j] = currLayer[i][j];
                currLayer[i][j] = -1;
            }
        }
    }
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        memset(prevLayer, -1, sizeof(prevLayer));        
        memset(currLayer, -1, sizeof(currLayer));
        prevLayer[0][n - 1] = grid[0][0] + grid[0][n - 1];

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
                            int prev = prevLayer[prevC1][prevC2];
                            if(prev != -1) {
                               highest = max(highest, prevLayer[prevC1][prevC2]);
                            }
                        }
                    }
                    highest += grid[row][c1] + grid[row][c2];
                    currLayer[c1][c2] = highest;
                    ans = max(ans, highest);
                }
            }
            moveLayer();
        }
        
        return ans;
    }
};
