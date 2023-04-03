class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int left = 0;
        int right = matrix[0].size() - 1;
        int up = 0;
        int down = matrix.size() - 1;
        vector<int> result;
        
        while (result.size() != matrix.size() * matrix[0].size()) {
            for (int i = left; i < right + 1; i++) {
                cout << 'A' << i;
                result.push_back(matrix[up][i]);
            }
                
            for (int j = up + 1; j < down + 1; j++) {
                cout << 'B';
                result.push_back(matrix[j][right]);
            }
                 
            if (up < down and left < right) {
                for (int i = right - 1; i > left - 1; i--) {
                    cout << 'c';
                    result.push_back(matrix[down][i]);
                }

                for (int j = down - 1; j > up; j--) {
                    cout << 'd';
                    result.push_back(matrix[j][left]);
                }
            }
            cout << endl;
            
            left += 1;
            right -= 1;
            up += 1;
            down -= 1;
        }
        
        return result;
    }
};
