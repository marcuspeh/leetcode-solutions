class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> cache;
        for (auto task: tasks) cache[task]++;
        
        int m = 0;
        vector<int> counts;
        for (auto [task, count]: cache) {
            counts.push_back(count);
            m = max(m, count);
        }
        
        int maxTaskCount = 0;
        for (auto count: counts) {
            if (count != m) continue;
            maxTaskCount++;
        }
        
        int temp = (m - 1) * (n + 1) + maxTaskCount;
        
        if (tasks.size() > temp) return tasks.size();
        return temp;
    }
};

       
       
       
    
