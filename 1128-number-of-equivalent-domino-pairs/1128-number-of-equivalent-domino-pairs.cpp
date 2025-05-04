class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> cache;
        int result = 0;
        for (vector<int>& domino: dominoes) {
            int dom = getKey(domino);
            if (!cache.count(dom)) {
                cache[dom] = 0;
            }
            result += cache[dom];
            cache[dom] += 1;
        }

        return result;
    }

    int getKey(vector<int>& domino) {
        int smaller = min(domino[0], domino[1]);
        int larger = max(domino[0], domino[1]);
        return larger * 10 + smaller;
    }
};