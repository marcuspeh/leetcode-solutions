class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        ds = [0] + [1] * (k + 1)
        for j in range(2, n + 1):
            new = [0]
            for i in range(k + 1):
                v = ds[i + 1]
                v -= ds[i - j + 1] if i >= j else 0
                new.append((new[-1] + v) % MOD)
            ds = new
        return (ds[k + 1] - ds[k]) % MOD