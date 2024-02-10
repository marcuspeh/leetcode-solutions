class Solution {
    const int NOT_VISITED = 0;
    const int VISITING = 1;
    const int VISITED = 2;
    
    bool visitCourse(int course, vector<int>& status, unordered_map<int, vector<int>>& nextMod) {
        if (status[course] == VISITED) {
            return true;
        }
        if (status[course] == VISITING) {
            return false;
        }
        
        status[course] = VISITING;
        for (auto followingMod: nextMod[course]) {
            bool isValid = visitCourse(followingMod, status, nextMod);
            if (!isValid) {
                return false;
            }
        }
        
        status[course] = VISITED;
        return true;
    }
    
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_set<int> startingCourse;
        for (int i = 0; i < numCourses; i++) {
            startingCourse.insert(i);
        }
        
        unordered_map<int, vector<int>> nextMod;
        for (auto prerequisite: prerequisites) {
            nextMod[prerequisite.back()].push_back(prerequisite.front());
            
            if (startingCourse.count(prerequisite.front()) > 0) {
                startingCourse.erase(prerequisite.front());
            }
        }
        
        vector<int> status(numCourses, NOT_VISITED);
        for (auto mod: startingCourse) {
            bool isValid = visitCourse(mod, status, nextMod);
            if (!isValid) {
                return false;
            }
        }
        
        for (auto mod: status) {
            if (mod != VISITED) {
                return false;
            }
        }
        return true;
    }
};