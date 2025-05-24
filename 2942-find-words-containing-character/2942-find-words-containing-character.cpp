class Solution {
    bool containWord(string& word, char x) {
        for (char letter: word) {
            if (letter == x) {
                return true;
            }
        }
        return false;
    }
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> result;
        for (int i = 0; i < words.size(); i++) {
            if (containWord(words[i], x)) {
                result.push_back(i);
            }
        }

        return move(result);
    }
};