class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (auto num: nums) {
            count[num] += 1;
        }
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto [number, count]: count) {
            pq.push({count, number});
            
            if (pq.size() > k) {
                pq.pop();
            }
        }
        
        vector<int> result;
        while (!pq.empty()) {
            pair<int, int> top = pq.top();
            result.push_back(top.second);
            pq.pop();
        }
        return result;
    }
};