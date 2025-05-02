class Solution {
public:
    string pushDominoes(string dominoes) {
        vector<char> result;

        int rightCount = 0;
        bool foundRight = false;
        for (char character: dominoes) {
            if (character == '.') {
                rightCount++;
                if (foundRight) {
                    result.push_back('R');
                    continue;
                } 

                result.push_back('.');
                continue;
            }

            if (character == 'R') {
                foundRight = true;
                rightCount = 0;
                result.push_back('R');
                continue;
            }

            int width = rightCount;
            if (foundRight) {
               width = rightCount / 2;
            } 

            for (int i = 1; i <= width; i++) {
                result[result.size() - i] = 'L';
            }

            if (foundRight && rightCount % 2) {
                result[result.size() - width - 1] = '.';
            }

            result.push_back('L');
            rightCount = 0;
            foundRight = false;
        }

        string output = "";
        for (char character: result) {
            output += character;
        }

        return output;
    }
};