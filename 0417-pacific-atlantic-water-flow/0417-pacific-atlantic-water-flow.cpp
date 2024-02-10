class Solution {
    vector<vector<bool>> visitFromFrontier(vector<vector<int>>& heights, vector<pair<int, int>>& frontier) {
        vector<vector<bool>> visited;
        for (auto row: heights) {
            vector<bool> visitedVector(row.size(), false);
            visited.push_back(visitedVector);
        }
        
        for (auto [i, j]: frontier) {
            visited[i][j] = true;
        }
        
        vector<pair<int, int>> direction = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        while (!frontier.empty()) {
            auto [i, j] = frontier.back();
            frontier.pop_back();
            
            for (auto [x, y]: direction) {
                int newI = i + x;
                int newJ = j + y;
                
                if (newI < 0 || newI >= heights.size()) {
                    continue;
                }
                if (newJ < 0 || newJ >= heights[0].size()) {
                    continue;
                }
                if (heights[newI][newJ] < heights[i][j] || visited[newI][newJ]) {
                    continue;
                }
                visited[newI][newJ] = true;
                frontier.push_back({newI, newJ});
            }
        }
        
        return visited;
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<pair<int, int>> pacific;
        vector<pair<int, int>> atlantic;
        for (int i = 0; i < heights.size(); i++) {
            pacific.push_back({i, 0});
            atlantic.push_back({i, heights[0].size() - 1});
        }
        for (int i = 0; i < heights[0].size(); i++) {
            pacific.push_back({0, i});
            atlantic.push_back({heights.size() - 1, i});
        }
        
        auto visitedPacific = visitFromFrontier(heights, pacific);
        auto visitedAtlantic = visitFromFrontier(heights, atlantic);
        
        vector<vector<int>> result;
        for (int i = 0; i < heights.size(); i++) {
            for (int j = 0; j < heights[i].size(); j++) {
                if (!visitedPacific[i][j] || !visitedAtlantic[i][j]) {
                    continue;
                }
                result.push_back(vector<int>({i, j}));
            }
        }
        return result;
    }
};