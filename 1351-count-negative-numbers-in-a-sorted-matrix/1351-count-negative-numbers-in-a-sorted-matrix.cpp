class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int i = grid.size() - 1;
        int j = 0;
        int rowSize = grid.at(0).size();
        
        int result = 0;
        
        while (i >= 0 && j < rowSize) {
            if (grid.at(i).at(j) < 0) {
                result += rowSize - j;
                i -= 1;
            } else {
                j += 1;
            }
        }
        
        return result;
    }
};