class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def dfs(start):
            if start >= len(s):
                return 0

            count = Counter()
            result = float('inf')

            for i in range(start, len(s)):
                count[s[i]] += 1
                if len(set(count.values())) == 1: 
                    result = min(result, dfs(i + 1) + 1)

            return result

        return dfs(0)