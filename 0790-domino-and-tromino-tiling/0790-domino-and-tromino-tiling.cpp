class Solution {
public:
    int numTilings(int n) {
        if (n <= 1) return 1;
        if (n == 2) return 2;
        if (n == 3) return 5;

        int a = 1;
        int b = 2;
        int c = 5;
        int mod = 1e9 + 7;

        for (int i = 4; i <= n; i++) {
            int curr = (c * 2 + a) % mod;
            a = b;
            b = c;
            c = curr;
        }
        
        return c;
    }
};