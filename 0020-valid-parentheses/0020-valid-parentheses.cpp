class Solution {
public:
    bool isValid(string s) {
        stack<char> checker;
        unordered_set<char> opening = {'(', '{', '['};
        unordered_map<char, char> match = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        for (char character: s) {
            if (opening.count(character)) {
                checker.push(character);
            } else {
                char matchingPair = match[character];
                if (checker.size() == 0 || matchingPair != checker.top()) {
                    return false;
                }
                checker.pop();
            }
        }
        
        return checker.size() == 0;
    }
};