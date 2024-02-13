class Solution {
    bool isPalindrome(string& word) {
        int start = 0;
        int end = word.size() - 1;
        
        while (start < end) {
            if (word[start] != word[end]) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
public:
    string firstPalindrome(vector<string>& words) {
        for (auto word: words) {
            if (isPalindrome(word)) {
                return word;
            }
        }
        return "";
    }
};