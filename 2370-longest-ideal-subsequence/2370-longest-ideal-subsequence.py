class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}
        result = 0
        for character in s:
            num = ord(character)
            
            largest = 1
            for i in range(num - k, num + k + 1):
                if i not in cache:
                    continue
                largest = max(largest, cache[i] + 1) 
            result = max(result, largest)
            cache[num] = largest
        return result
            