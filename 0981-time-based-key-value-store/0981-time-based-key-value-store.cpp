class TimeMap {
private:
    unordered_map<string, vector<pair<string, int>>> store;
    
public:
    TimeMap() {
  
    }
    
    void set(string key, string value, int timestamp) {
        store[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if (store.count(key) == 0) return "";
        
        if (timestamp < store[key][0].second) return "";
        
        int start = 0;
        int end = store[key].size();
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (store[key][mid].second <= timestamp) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        
        if (start == 0) {
            return "";
        }
        
        return store[key][start - 1].first;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */