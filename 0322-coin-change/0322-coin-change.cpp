class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Either take or dont take
        // If take, table[amount - coin] + 1
        // else, 0
        if (amount == 0) return 0;
        
        int table[amount + 1];
        // memset(table, INT_MAX, sizeof(table));
        for (int i = 1; i <= amount; i++) table[i] = INT_MAX;
        table[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int coin: coins) {
                if (i >= coin && table[i - coin] != INT_MAX) {
                    table[i] = min(table[i], table[i - coin] + 1);
                }
            }
        }
        
        return table[amount] < INT_MAX? table[amount] : -1;
    }
};