class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        maxCount = 0
        start = 0
        for i in range(len(s)):
            if s[i] in count:
                start = max(start, count[s[i]] + 1)
            count[s[i]] = i
            maxCount = max(maxCount, i - start + 1)
        return maxCount
                