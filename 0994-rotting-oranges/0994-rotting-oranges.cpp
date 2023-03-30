class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int fresh = 0;
        vector<pair<int, int>> frontier;
        
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 1) {
                    fresh++;
                } else if (grid[i][j] == 2) {
                    frontier.push_back({i, j});
                }
            }
        }
        
        int moves[4][2] = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        
        int result = 0;
        
        while (fresh > 0 && !frontier.empty()) {
            vector<pair<int, int>> newFrontier;
            
            for (auto [i, j]: frontier) {
                for (auto move: moves) {
                    int newI = i + move[0];
                    int newJ = j + move[1];
                    
                    if (newI < 0 || newI >= grid.size()) {
                        continue;
                    }
                    
                    if (newJ < 0 || newJ >= grid[0].size()) {
                        continue;
                    }
                    
                    if (grid[newI][newJ] != 1) {
                        continue;
                    } 
                    
                    fresh--;
                    grid[newI][newJ] = 2;
                    newFrontier.push_back({newI, newJ});                   
                }
            }
            
            swap(frontier, newFrontier);
            result++;
        }
        
        return fresh > 0 ? -1 : result;
    }
};