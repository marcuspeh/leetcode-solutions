class State {
    public:
    int x;
    int y;
    int cost;

    State(int x, int y, int cost) {
        this->x = x;
        this->y = y;
        this->cost = cost;
    }
};

class Comp {
public:
    bool operator()(State& a, State&b) {
        return a.cost > b.cost;
    }
};

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        vector<vector<bool>> seen {
            moveTime.size(),
            vector<bool>(moveTime[0].size(), false)
        };

        vector<pair<int, int>> moves {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1},
        };

        priority_queue<State, vector<State>, Comp> pq;
        pq.push(State(0, 0, 0));

        while (!pq.empty()) {
            State curr = pq.top();
            if (curr.x == moveTime.size() - 1 && curr.y == moveTime[0].size() - 1) {
                return curr.cost;
            }
            pq.pop();

            if (seen[curr.x][curr.y]) {
                continue;
            }
            seen[curr.x][curr.y] = true;
            
            for (auto [changeX, changeY]: moves) {
                int newX = curr.x + changeX;
                int newY = curr.y + changeY;

                if (newX < 0 ||  newX >= moveTime.size()) {
                    continue;
                }
                if (newY < 0 || newY >= moveTime[0].size()) {
                    continue;
                }
                if (seen[newX][newY]) {
                    continue;
                }

                int newCost = max(curr.cost, moveTime[newX][newY]) + 1;
                pq.push(State(newX, newY, newCost));
            }
            
        }

        return INT_MAX;
    }
};