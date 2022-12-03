class Solution:
    def frequencySort(self, s: str) -> str:
        cache = {}
        for character in s:
            if character not in cache:
                cache[character] = 0
            cache[character] += 1
        
        sortedArray = sorted(cache.items(), key=lambda x: x[1], reverse=True)
        result = "".join([character * freq for character, freq in sortedArray])
        return result