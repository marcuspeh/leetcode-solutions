class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        maxOdd = float("-inf")
        minEven = float("inf")
        for char, count in freq.items():
            if count % 2:
                maxOdd = max(maxOdd, count)
                continue
                
            minEven = min(minEven, count)
        return maxOdd - minEven