class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> cache;
        int result = 0;

        for (string word: words) {
            string reverseWord = word.substr(1, 1) + word.substr(0, 1);
            if (cache.count(reverseWord) > 0) {
                result += 4;
                cache[reverseWord]--;

                if (cache[reverseWord] == 0) {
                    cache.erase(reverseWord);
                }
                continue;
            }

            if (cache.count(word) == 0) {
                cache[word] = 0;
            }
            cache[word]++;
        }

        for (auto[word, _] : cache) {
            if (word[0] == word[1]) {
                result += 2;
                break;
            }
        }

        return result;
    }
};